from pathlib import Path
import sys
import os
import dotenv
from datetime import datetime, timedelta
import re

# Ensure project root is on sys.path so `utils` can be imported when running directly
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.interface import get_google_news

# Load environment variables from .env
dotenv.load_dotenv()

def market_sentiment_analysis():
    """
    Use case: Analyze market sentiment through news headlines
    """
    print("=== Market Sentiment Analysis ===\n")
    
    curr_date = datetime.now().strftime("%Y-%m-%d")
    
    # Keywords that typically indicate positive/negative sentiment
    positive_keywords = ['bullish', 'rally', 'surge', 'gain', 'positive', 'growth', 'profit']
    negative_keywords = ['bearish', 'crash', 'drop', 'loss', 'negative', 'decline', 'risk']
    
    # Fetch news for market sentiment analysis
    sentiment_queries = [
        "stock market sentiment",
        "market outlook",
        "investor confidence",
        "market volatility",
        "trading sentiment"
    ]
    
    all_news = ""
    for query in sentiment_queries:
        try:
            result = get_google_news(query, curr_date, look_back_days=3)
            all_news += result + "\n"
        except Exception as e:
            print(f"Error fetching {query}: {e}")
    
    # Analyze sentiment
    positive_count = sum(1 for keyword in positive_keywords if keyword.lower() in all_news.lower())
    negative_count = sum(1 for keyword in negative_keywords if keyword.lower() in all_news.lower())
    
    print(f"Positive sentiment indicators: {positive_count}")
    print(f"Negative sentiment indicators: {negative_count}")
    
    if positive_count > negative_count:
        print("Overall sentiment: BULLISH")
    elif negative_count > positive_count:
        print("Overall sentiment: BEARISH")
    else:
        print("Overall sentiment: NEUTRAL")
    
    return all_news

def competitor_monitoring():
    """
    Use case: Monitor competitors through news tracking
    """
    print("\n=== Competitor Monitoring ===\n")
    
    curr_date = datetime.now().strftime("%Y-%m-%d")
    
    # Define company and their main competitors
    companies = {
        "Apple": ["Samsung", "Google", "Microsoft", "Amazon"],
        "Tesla": ["Ford", "GM", "Toyota", "Volkswagen", "BYD"],
        "Netflix": ["Disney+", "Amazon Prime", "Hulu", "HBO Max"]
    }
    
    for company, competitors in companies.items():
        print(f"\n--- {company} Competitor Analysis ---")
        
        # Get news for the main company
        try:
            company_news = get_google_news(company, curr_date, look_back_days=7)
            print(f"✓ {company} news fetched")
        except Exception as e:
            print(f"✗ Error fetching {company} news: {e}")
            continue
        
        # Get news for competitors
        competitor_news = {}
        for competitor in competitors:
            try:
                news = get_google_news(competitor, curr_date, look_back_days=7)
                competitor_news[competitor] = news
                print(f"✓ {competitor} news fetched")
            except Exception as e:
                print(f"✗ Error fetching {competitor} news: {e}")
        
        # Simple analysis - count mentions
        print(f"\nNews mentions in last 7 days:")
        print(f"  {company}: {company_news.count('###')} articles")
        for comp, news in competitor_news.items():
            print(f"  {comp}: {news.count('###')} articles")

def trend_detection():
    """
    Use case: Detect emerging trends through news frequency analysis
    """
    print("\n=== Trend Detection ===\n")
    
    curr_date = datetime.now().strftime("%Y-%m-%d")
    
    # Emerging technology trends to monitor
    trends = [
        "artificial intelligence",
        "blockchain",
        "quantum computing",
        "5G technology",
        "electric vehicles",
        "renewable energy",
        "biotechnology",
        "cybersecurity"
    ]
    
    trend_data = {}
    
    for trend in trends:
        print(f"Analyzing trend: {trend}")
        
        # Get recent news (last 7 days)
        try:
            recent_news = get_google_news(trend, curr_date, look_back_days=7)
            recent_count = recent_news.count('###')
        except Exception as e:
            print(f"  Error: {e}")
            recent_count = 0
        
        # Get older news (last 30 days) for comparison
        try:
            older_news = get_google_news(trend, curr_date, look_back_days=30)
            older_count = older_news.count('###')
        except Exception as e:
            print(f"  Error: {e}")
            older_count = 0
        
        # Calculate trend intensity
        if older_count > 0:
            trend_intensity = (recent_count / 7) / (older_count / 30)
        else:
            trend_intensity = 0
        
        trend_data[trend] = {
            "recent_7_days": recent_count,
            "older_30_days": older_count,
            "trend_intensity": trend_intensity
        }
        
        print(f"  Recent (7d): {recent_count}, Older (30d): {older_count}, Intensity: {trend_intensity:.2f}")
    
    # Identify hottest trends
    print(f"\n--- Trend Ranking ---")
    sorted_trends = sorted(trend_data.items(), key=lambda x: x[1]['trend_intensity'], reverse=True)
    
    for i, (trend, data) in enumerate(sorted_trends[:5], 1):
        print(f"{i}. {trend}: Intensity {data['trend_intensity']:.2f}")
    
    return trend_data

def earnings_analysis():
    """
    Use case: Analyze earnings-related news and sentiment
    """
    print("\n=== Earnings Analysis ===\n")
    
    curr_date = datetime.now().strftime("%Y-%m-%d")
    
    # Companies with recent or upcoming earnings
    earnings_companies = [
        "Apple earnings",
        "Microsoft earnings", 
        "Tesla earnings",
        "Amazon earnings",
        "Google earnings"
    ]
    
    earnings_data = {}
    
    for company_earnings in earnings_companies:
        print(f"Analyzing: {company_earnings}")
        
        try:
            # Get news from last 14 days (earnings cycle)
            news = get_google_news(company_earnings, curr_date, look_back_days=14)
            
            # Extract company name
            company = company_earnings.split()[0]
            
            # Count articles
            article_count = news.count('###')
            
            # Look for specific earnings-related keywords
            earnings_keywords = ['beat', 'miss', 'expectations', 'guidance', 'revenue', 'profit']
            keyword_counts = {}
            
            for keyword in earnings_keywords:
                count = len(re.findall(rf'\b{keyword}\b', news, re.IGNORECASE))
                if count > 0:
                    keyword_counts[keyword] = count
            
            earnings_data[company] = {
                "article_count": article_count,
                "keyword_counts": keyword_counts,
                "news": news
            }
            
            print(f"  Articles: {article_count}")
            print(f"  Key terms: {keyword_counts}")
            
        except Exception as e:
            print(f"  Error: {e}")
    
    return earnings_data

def sector_rotation_analysis():
    """
    Use case: Analyze sector rotation through news flow
    """
    print("\n=== Sector Rotation Analysis ===\n")
    
    curr_date = datetime.now().strftime("%Y-%m-%d")
    
    # Major market sectors
    sectors = [
        "technology sector",
        "financial sector", 
        "healthcare sector",
        "energy sector",
        "consumer discretionary",
        "industrial sector",
        "materials sector",
        "utilities sector"
    ]
    
    sector_data = {}
    
    for sector in sectors:
        print(f"Analyzing sector: {sector}")
        
        try:
            # Get news from last 5 days
            news = get_google_news(sector, curr_date, look_back_days=5)
            
            # Count articles
            article_count = news.count('###')
            
            # Look for momentum indicators
            momentum_keywords = ['rally', 'surge', 'breakout', 'momentum', 'strength']
            momentum_count = sum(len(re.findall(rf'\b{keyword}\b', news, re.IGNORECASE)) 
                               for keyword in momentum_keywords)
            
            sector_data[sector] = {
                "article_count": article_count,
                "momentum_score": momentum_count,
                "news": news
            }
            
            print(f"  Articles: {article_count}, Momentum score: {momentum_count}")
            
        except Exception as e:
            print(f"  Error: {e}")
    
    # Rank sectors by momentum
    print(f"\n--- Sector Momentum Ranking ---")
    sorted_sectors = sorted(sector_data.items(), key=lambda x: x[1]['momentum_score'], reverse=True)
    
    for i, (sector, data) in enumerate(sorted_sectors, 1):
        print(f"{i}. {sector}: {data['momentum_score']} momentum points")
    
    return sector_data

def main():
    """
    Run all use case examples
    """
    print("Google News API - Use Case Examples")
    print("=" * 50)
    
    try:
        # Run different use cases
        sentiment_news = market_sentiment_analysis()
        competitor_monitoring()
        trend_data = trend_detection()
        earnings_data = earnings_analysis()
        sector_data = sector_rotation_analysis()
        
        print("\n" + "=" * 50)
        print("All use case examples completed successfully!")
        print("=" * 50)
        
        # Summary
        print(f"\nSummary:")
        print(f"- Market sentiment analyzed")
        print(f"- Competitor monitoring completed") 
        print(f"- {len(trend_data)} trends analyzed")
        print(f"- {len(earnings_data)} earnings analyses completed")
        print(f"- {len(sector_data)} sectors analyzed")
        
    except Exception as e:
        print(f"Error running use case examples: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 