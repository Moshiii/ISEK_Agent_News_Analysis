#!/usr/bin/env python3
"""
Demo script for the hexun_news function from futurenews_hexun_utils.py

This script demonstrates various ways to use the hexun_news function
to filter and search through the hexun integrated news CSV file.
"""

import sys
import os

# Add the parent directory to the path so we can import the utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from futurenews_hexun_utils import hexun_news

def demo_hexun_news():
    """Demonstrate usage of the hexun_news function with various filters."""
    print("=== Hexun News Filter Demo ===\n")
    
    # Example 1: Get all news
    print("1. All news (first 5 items):")
    all_news = hexun_news()
    for item in all_news[:5]:
        print(f"  {item}")
        print()
    
    # Example 2: Filter by query
    print("2. News containing '焦煤' (coking coal):")
    coking_news = hexun_news(query="焦煤")
    for item in coking_news[:3]:
        print(f"  {item}")
        print()
    
    # Example 3: Filter by date range
    print("3. News from 2025-08-26:")
    today_news = hexun_news(start_date="2025-08-26", end_date="2025-08-26")
    print(f"  Found {len(today_news)} items for today")
    if today_news:
        print(f"  First item: {today_news[0]}")
    
    # Example 4: Combined filter
    print("\n4. News containing '期货' (futures) from today:")
    futures_today = hexun_news(query="期货", start_date="2025-08-26", end_date="2025-08-26")
    print(f"  Found {len(futures_today)} items")
    if futures_today:
        print(f"  First item: {futures_today[0]}")
    
    # Example 5: Search for specific commodities
    print("\n5. News about '原油' (crude oil):")
    oil_news = hexun_news(query="原油")
    print(f"  Found {len(oil_news)} items about crude oil")
    if oil_news:
        print(f"  First item: {oil_news[0]}")
    
    # Example 6: Date range search
    print("\n6. News from the last few days (if available):")
    recent_news = hexun_news(start_date="2025-08-25", end_date="2025-08-26")
    print(f"  Found {len(recent_news)} items from recent dates")
    if recent_news:
        print(f"  First item: {recent_news[0]}")

if __name__ == "__main__":
    demo_hexun_news() 