#!/usr/bin/env python3
"""
APITube News API Example

This example demonstrates how to fetch news articles using the APITube API.
You need to get an API key from https://apitube.io/
"""

import requests
import json
import os
from typing import Dict, List, Optional
import dotenv
dotenv.load_dotenv()

class APITubeClient:
    """Client for APITube News API"""
    
    def __init__(self, api_key: str):
        """
        Initialize APITube client
        
        Args:
            api_key: Your APITube API key
        """
        self.api_key = api_key 
        self.base_url = "https://api.apitube.io/v1"
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }
    
    
    
# https://api.apitube.io/v1/news/everything?title=btc&published_at.start=2025-01-01&published_at.end=2025-01-01&sort.order=desc&api_key=YOUR_API_KEY
    
    def get_news(self, per_page: int = 10, title: Optional[str] = None, 
                 language: str = "en", country: Optional[str] = None,
                 published_at_start: Optional[str] = None,
                 published_at_end: Optional[str] = None,
                 sort_order: str = "desc") -> Dict:
        """
        Fetch news articles from APITube
        
        Args:
            per_page: Number of articles to fetch (default: 10)
            query: Search query for specific topics
            language: Language code (default: "en")
            country: Country code for localized news
            
        Returns:
            Dictionary containing news articles and metadata
        """
        url = f"{self.base_url}/news/everything"
        
        params = {
            "per_page": per_page,
            "language": language,
            "published_at.start": published_at_start,
            "published_at.end": published_at_end,
            "sort.order": sort_order
        }
        
        if title:
            params["title"] = title
        if country:
            params["country"] = country
        if published_at_start:
            params["published_at.start"] = published_at_start
        if published_at_end:
            params["published_at.end"] = published_at_end
        if sort_order:
            params["sort.order"] = sort_order
        
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        
        return response.json()
    
    def get_top_headlines(self, country: str = "us", category: Optional[str] = None,
                         per_page: int = 10) -> Dict:
        """
        Fetch top headlines from APITube
        
        Args:
            country: Country code (default: "us")
            category: News category (business, technology, etc.)
            per_page: Number of articles to fetch
            
        Returns:
            Dictionary containing top headlines
        """
        url = f"{self.base_url}/news/top-headlines"
        
        params = {
            "country": country,
            "per_page": per_page
        }
        
        if category:
            params["category"] = category
        
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        
        return response.json()


def print_articles(articles: List[Dict], title: str = "News Articles"):
    """Pretty print news articles"""
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    
    if not articles:
        return
    
    for i, article in enumerate(articles, 1):
        print(f"\n{i}. {article.get('title', 'No title')}")
        print(f"   Source: {article.get('source', {}).get('domain', 'Unknown')}")
        print(f"   Published: {article.get('published_at', 'Unknown')}")
        print(f"   URL: {article.get('href', 'No URL')}")
        if article.get('description'):
            print(f"   Description: {article.get('description')[:100]}...")


def main():
    """Main example function"""
    # Get API key from environment variable or use placeholder
    api_key = os.getenv("APITUBE_API_KEY")
    
    if not api_key:
        print("Warning: APITUBE_API_KEY environment variable not set!")
        print("Please set your API key: export APITUBE_API_KEY='your_api_key_here'")
        api_key = "APITUBE_API_KEY"  # Placeholder
    
    # Initialize client
    client = APITubeClient(api_key)
    
    # Example 1: Get general news
    print("Fetching general news...")
    news_data = client.get_news(per_page=2)
    
    if news_data and 'results' in news_data:
        print_articles(news_data['results'], "General News")
        print(f"\nTotal articles available: {len(news_data.get('results', []))}")
    else:
        print("No news data received")
    
    # Example 2: Search for specific topic
    print("\n" + "="*60)
    print("Searching for technology news...")
    tech_news = client.get_news(title="technology", per_page=2)
    
    if tech_news and 'results' in tech_news:
        print_articles(tech_news['results'], "Technology News")
    
    # Example 3: Get top headlines
    print("\n" + "="*60)
    print("Fetching top US headlines...")
    headlines = client.get_top_headlines(country="us", per_page=2)
    
    if headlines and 'results' in headlines:
        print_articles(headlines['results'], "Top US Headlines")

    # Example 4: Search for crypto news
    print("\n" + "="*60)
    print("Searching for crypto news...")
    crypto_news = client.get_news(title="crypto", per_page=2)

    if crypto_news and 'results' in crypto_news:
        print_articles(crypto_news['results'], "Crypto News")
    else:
        print("No crypto news data received")

if __name__ == "__main__":
    main()