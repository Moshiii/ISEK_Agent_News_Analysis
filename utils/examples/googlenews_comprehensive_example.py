from pathlib import Path
import sys
import os
import dotenv
from datetime import datetime, timedelta
import json

# Ensure project root is on sys.path so `utils` can be imported when running directly
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.interface import get_google_news

# Load environment variables from .env
dotenv.load_dotenv()

class GoogleNewsAnalyzer:
    """
    A comprehensive example class demonstrating various ways to use get_google_news
    """
    
    def __init__(self):
        self.curr_date = datetime.now().strftime("%Y-%m-%d")
        self.results_cache = {}
    
    def fetch_company_news(self, company_name: str, look_back_days: int = 7) -> dict:
        """
        Fetch news for a specific company with error handling
        """
        print(f"Fetching news for {company_name} (last {look_back_days} days)...")
        
        try:
            result = get_google_news(
                query=company_name,
                curr_date=self.curr_date,
                look_back_days=look_back_days
            )
            
            # Store result in cache
            cache_key = f"{company_name}_{look_back_days}"
            self.results_cache[cache_key] = result
            
            return {
                "success": True,
                "company": company_name,
                "look_back_days": look_back_days,
                "result": result,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            error_info = {
                "success": False,
                "company": company_name,
                "look_back_days": look_back_days,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
            print(f"Error fetching news for {company_name}: {e}")
            return error_info
    
    def fetch_sector_news(self, sector: str, look_back_days: int = 7) -> dict:
        """
        Fetch news for a market sector
        """
        print(f"Fetching {sector} sector news (last {look_back_days} days)...")
        
        try:
            result = get_google_news(
                query=sector,
                curr_date=self.curr_date,
                look_back_days=look_back_days
            )
            
            return {
                "success": True,
                "sector": sector,
                "look_back_days": look_back_days,
                "result": result,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            error_info = {
                "success": False,
                "sector": sector,
                "look_back_days": look_back_days,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
            print(f"Error fetching {sector} sector news: {e}")
            return error_info
    
    def fetch_market_event_news(self, event: str, look_back_days: int = 7) -> dict:
        """
        Fetch news for specific market events
        """
        print(f"Fetching news for market event: {event} (last {look_back_days} days)...")
        
        try:
            result = get_google_news(
                query=event,
                curr_date=self.curr_date,
                look_back_days=look_back_days
            )
            
            return {
                "success": True,
                "event": event,
                "look_back_days": look_back_days,
                "result": result,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            error_info = {
                "success": False,
                "event": event,
                "look_back_days": look_back_days,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
            print(f"Error fetching news for {event}: {e}")
            return error_info
    
    def batch_fetch_news(self, queries: list, look_back_days: int = 7) -> list:
        """
        Fetch news for multiple queries in batch
        """
        print(f"Batch fetching news for {len(queries)} queries (last {look_back_days} days)...")
        
        results = []
        for i, query in enumerate(queries, 1):
            print(f"Processing query {i}/{len(queries)}: {query}")
            
            try:
                result = get_google_news(
                    query=query,
                    curr_date=self.curr_date,
                    look_back_days=look_back_days
                )
                
                results.append({
                    "success": True,
                    "query": query,
                    "look_back_days": look_back_days,
                    "result": result,
                    "timestamp": datetime.now().isoformat()
                })
                
            except Exception as e:
                results.append({
                    "success": False,
                    "query": query,
                    "look_back_days": look_back_days,
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                })
                print(f"Error processing query '{query}': {e}")
            
            # Add a small delay to avoid overwhelming the API
            import time
            time.sleep(0.5)
        
        return results
    
    def save_results_to_file(self, results: list, filename: str = None):
        """
        Save results to a JSON file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"googlenews_results_{timestamp}.json"
        
        filepath = Path(filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"Results saved to: {filepath}")
        except Exception as e:
            print(f"Error saving results to file: {e}")
    
    def print_summary(self, results: list):
        """
        Print a summary of the results
        """
        print("\n" + "="*60)
        print("GOOGLE NEWS FETCH SUMMARY")
        print("="*60)
        
        successful = [r for r in results if r.get("success", False)]
        failed = [r for r in results if not r.get("success", False)]
        
        print(f"Total queries: {len(results)}")
        print(f"Successful: {len(successful)}")
        print(f"Failed: {len(failed)}")
        
        if failed:
            print(f"\nFailed queries:")
            for result in failed:
                print(f"  - {result.get('query', 'Unknown')}: {result.get('error', 'Unknown error')}")
        
        print("="*60)

def comprehensive_example():
    """
    Comprehensive example demonstrating various Google News API usage patterns
    """
    print("=== Comprehensive Google News Example ===\n")
    
    analyzer = GoogleNewsAnalyzer()
    
    # Example 1: Company-specific news with different time periods
    print("1. Company News Analysis")
    print("-" * 40)
    
    companies = ["Apple", "Microsoft", "Google", "Amazon", "Tesla"]
    company_results = []
    
    for company in companies:
        result = analyzer.fetch_company_news(company, look_back_days=7)
        company_results.append(result)
        print(f"✓ {company} news fetched")
    
    # Example 2: Sector analysis
    print("\n2. Sector News Analysis")
    print("-" * 40)
    
    sectors = ["technology sector", "financial sector", "healthcare sector", "energy sector"]
    sector_results = []
    
    for sector in sectors:
        result = analyzer.fetch_sector_news(sector, look_back_days=5)
        sector_results.append(result)
        print(f"✓ {sector} news fetched")
    
    # Example 3: Market events
    print("\n3. Market Event News")
    print("-" * 40)
    
    events = ["Federal Reserve", "earnings season", "market volatility", "IPO market"]
    event_results = []
    
    for event in events:
        result = analyzer.fetch_market_event_news(event, look_back_days=3)
        event_results.append(result)
        print(f"✓ {event} news fetched")
    
    # Example 4: Batch processing
    print("\n4. Batch News Processing")
    print("-" * 40)
    
    batch_queries = [
        "stock market today",
        "cryptocurrency news",
        "bond yields",
        "oil prices",
        "gold market"
    ]
    
    batch_results = analyzer.batch_fetch_news(batch_queries, look_back_days=2)
    
    # Combine all results
    all_results = company_results + sector_results + event_results + batch_results
    
    # Print summary
    analyzer.print_summary(all_results)
    
    # Save results to file
    analyzer.save_results_to_file(all_results)
    
    return all_results

def practical_scenarios():
    """
    Demonstrate practical use cases for the Google News API
    """
    print("\n=== Practical Use Cases ===\n")
    
    analyzer = GoogleNewsAnalyzer()
    
    # Scenario 1: Daily market monitoring
    print("Scenario 1: Daily Market Monitoring")
    print("-" * 40)
    
    daily_queries = [
        "S&P 500",
        "NASDAQ",
        "Dow Jones",
        "market sentiment",
        "trading volume"
    ]
    
    daily_results = analyzer.batch_fetch_news(daily_queries, look_back_days=1)
    print(f"✓ Daily market monitoring completed: {len(daily_results)} queries")
    
    # Scenario 2: Company earnings focus
    print("\nScenario 2: Company Earnings Focus")
    print("-" * 40)
    
    earnings_queries = [
        "Apple earnings",
        "Microsoft earnings",
        "Tesla earnings",
        "earnings report",
        "quarterly results"
    ]
    
    earnings_results = analyzer.batch_fetch_news(earnings_queries, look_back_days=14)
    print(f"✓ Earnings focus completed: {len(earnings_results)} queries")
    
    # Scenario 3: Economic indicators
    print("\nScenario 3: Economic Indicators")
    print("-" * 40)
    
    economic_queries = [
        "inflation data",
        "unemployment rate",
        "GDP growth",
        "interest rates",
        "Federal Reserve policy"
    ]
    
    economic_results = analyzer.batch_fetch_news(economic_queries, look_back_days=7)
    print(f"✓ Economic indicators completed: {len(economic_results)} queries")
    
    return daily_results + earnings_results + economic_results

def main():
    """
    Run all comprehensive examples
    """
    try:
        # Run comprehensive example
        comprehensive_results = comprehensive_example()
        
        # Run practical scenarios
        practical_results = practical_scenarios()
        
        # Final summary
        print("\n" + "="*60)
        print("ALL EXAMPLES COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"Total results processed: {len(comprehensive_results) + len(practical_results)}")
        print("Check the generated JSON files for detailed results.")
        
    except Exception as e:
        print(f"Error running examples: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 