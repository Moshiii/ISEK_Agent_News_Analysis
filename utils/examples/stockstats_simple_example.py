from pathlib import Path
import sys
import os
import dotenv

# Ensure project root is on sys.path so `utils` can be imported when running directly
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.interface import get_stock_stats_indicators_window

# Load environment variables from .env
dotenv.load_dotenv()

def simple_example():
    """
    Simple example showing basic usage of get_stock_stats_indicators_window
    """
    print("=== Simple Stock Stats Indicators Example ===\n")
    
    # Basic parameters
    symbol = "AAPL"
    curr_date = "2024-03-01"
    look_back_days = 14
    
    print(f"Symbol: {symbol}")
    print(f"Current Date: {curr_date}")
    print(f"Look Back Days: {look_back_days}\n")
    
    # Example 1: Get RSI indicator (online)
    print("--- Getting RSI Indicator (Online) ---")
    try:
        result = get_stock_stats_indicators_window(
            symbol=symbol,
            indicator="rsi",
            curr_date=curr_date,
            look_back_days=look_back_days,
            online=True
        )
        print(result)
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "-" * 50 + "\n")
    
    # Example 2: Get 50-day SMA (online)
    print("--- Getting 50-Day SMA (Online) ---")
    try:
        result = get_stock_stats_indicators_window(
            symbol=symbol,
            indicator="close_50_sma",
            curr_date=curr_date,
            look_back_days=look_back_days,
            online=True
        )
        print(result)
    except Exception as e:
        print(f"Error: {e}")

def offline_example():
    """
    Example showing offline usage (requires local data files)
    """
    print("\n=== Offline Mode Example ===\n")
    
    symbol = "AAPL"
    curr_date = "2024-03-01"
    look_back_days = 7
    
    print(f"Symbol: {symbol}")
    print(f"Current Date: {curr_date}")
    print(f"Look Back Days: {look_back_days}")
    print("Note: This requires local data files to be present\n")
    
    try:
        result = get_stock_stats_indicators_window(
            symbol=symbol,
            indicator="macd",
            curr_date=curr_date,
            look_back_days=look_back_days,
            online=False
        )
        print("--- MACD Indicator (Offline) ---")
        print(result)
    except Exception as e:
        print(f"Error (offline mode): {e}")
        print("This is expected if local data files are not available")

def available_indicators():
    """
    Show all available technical indicators
    """
    print("\n=== Available Technical Indicators ===\n")
    
    indicators = {
        "Moving Averages": ["close_50_sma", "close_200_sma", "close_10_ema"],
        "MACD": ["macd", "macds", "macdh"],
        "Momentum": ["rsi"],
        "Volatility": ["boll", "boll_ub", "boll_lb", "atr"],
        "Volume": ["vwma", "mfi"]
    }
    
    for category, inds in indicators.items():
        print(f"{category}:")
        for ind in inds:
            print(f"  - {ind}")
        print()

if __name__ == "__main__":
    # Run the simple example
    simple_example()
    
    # Show available indicators
    available_indicators()
    
    # Try offline mode (may fail if no local data)
    offline_example() 