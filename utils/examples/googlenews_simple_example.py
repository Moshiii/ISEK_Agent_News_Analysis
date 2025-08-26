from pathlib import Path
import sys
import os
import dotenv
from datetime import datetime, timedelta

# Ensure project root is on sys.path so `utils` can be imported when running directly
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.interface import get_google_news

# Load environment variables from .env
dotenv.load_dotenv()

def simple_example():
    """
    Simple example showing basic usage of get_google_news
    """
    print("=== Simple Google News Example ===\n")
    
    # Basic parameters
    curr_date = datetime.now().strftime("%Y-%m-%d")
    look_back_days = 7
    
    print(f"Current Date: {curr_date}")
    print(f"Look Back Days: {look_back_days}\n")
    
    # Example 1: Company-specific news
    print("--- Apple Inc. News ---")
    try:
        result = get_google_news(
            query="Apple Inc",
            curr_date=curr_date,
            look_back_days=look_back_days
        )
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "-" * 50 + "\n")
    
    # Example 2: Market sector news
    print("--- Technology Sector News ---")
    try:
        result = get_google_news(
            query="technology sector",
            curr_date=curr_date,
            look_back_days=look_back_days
        )
        print(result)
    except Exception as e:
        print(f"Error: {e}")

def date_range_examples():
    """
    Examples with different date ranges
    """
    print("\n=== Date Range Examples ===\n")
    
    curr_date = datetime.now().strftime("%Y-%m-%d")
    
    # Different look-back periods
    periods = [1, 3, 7, 14, 30]
    
    for days in periods:
        print(f"--- Tesla News (Last {days} days) ---")
        try:
            result = get_google_news(
                query="Tesla",
                curr_date=curr_date,
                look_back_days=days
            )
            print(result)
        except Exception as e:
            print(f"Error: {e}")
        
        print("\n" + "-" * 30 + "\n")

def query_variations():
    """
    Examples with different query types
    """
    print("\n=== Query Variation Examples ===\n")
    
    curr_date = datetime.now().strftime("%Y-%m-%d")
    look_back_days = 7
    
    queries = [
        "Tesla stock",
        "TSLA",
        "electric vehicles",
        "EV market",
        "Tesla earnings",
        "Tesla CEO Elon Musk"
    ]
    
    for query in queries:
        print(f"--- Query: '{query}' ---")
        try:
            result = get_google_news(
                query=query,
                curr_date=curr_date,
                look_back_days=look_back_days
            )
            print(result)
        except Exception as e:
            print(f"Error: {e}")
        
        print("\n" + "-" * 40 + "\n")

def main():
    """
    Run all examples
    """
    simple_example()
    date_range_examples()
    query_variations()

if __name__ == "__main__":
    main() 