from pathlib import Path
import sys
import os
import dotenv
from datetime import datetime, timedelta

# Ensure project root is on sys.path so `utils` can be imported when running directly
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.interface import get_stock_stats_indicators_window

# Load environment variables from .env
dotenv.load_dotenv()
DATA_DIR = os.getenv("DATA_DIR")

def main() -> None:
    """
    Example usage of get_stock_stats_indicators_window function.
    
    This function retrieves technical indicator values for a given stock symbol
    over a specified time window, with options for online/offline data fetching.
    """
    
    # Example parameters
    symbol = "AAPL"  # Apple Inc.
    curr_date = "2024-03-01"  # Current trading date
    look_back_days = 30  # Look back 30 days
    
    # Available technical indicators
    indicators = [
        # Moving Averages
        "close_50_sma",    # 50-day Simple Moving Average
        "close_200_sma",   # 200-day Simple Moving Average  
        "close_10_ema",    # 10-day Exponential Moving Average
        
        # MACD Related
        "macd",            # MACD Line
        "macds",           # MACD Signal Line
        "macdh",           # MACD Histogram
        
        # Momentum Indicators
        "rsi",             # Relative Strength Index
        
        # Volatility Indicators
        "boll",            # Bollinger Bands Middle
        "boll_ub",         # Bollinger Bands Upper
        "boll_lb",         # Bollinger Bands Lower
        "atr",             # Average True Range
        
        # Volume-Based Indicators
        "vwma",            # Volume Weighted Moving Average
        "mfi",             # Money Flow Index
    ]
    
    print(f"=== Stock Stats Indicators Example for {symbol} ===\n")
    print(f"Date Range: {curr_date} to {look_back_days} days back")
    print(f"Total Indicators Available: {len(indicators)}\n")
    
    # Example 1: Get a single indicator (offline mode)
    print("--- Example 1: Single Indicator (Offline Mode) ---")
    try:
        result = get_stock_stats_indicators_window(
            symbol=symbol,
            indicator="rsi",
            curr_date=curr_date,
            look_back_days=look_back_days,
            online=False
        )
        print(result)
    except Exception as e:
        print(f"Error getting RSI indicator (offline): {e}")
    
    print("\n" + "="*80 + "\n")
    
    # Example 2: Get a moving average indicator (online mode)
    print("--- Example 2: Moving Average Indicator (Online Mode) ---")
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
        print(f"Error getting 50 SMA indicator (online): {e}")
    
    print("\n" + "="*80 + "\n")
    
    # Example 3: Get MACD indicator (online mode)
    print("--- Example 3: MACD Indicator (Online Mode) ---")
    try:
        result = get_stock_stats_indicators_window(
            symbol=symbol,
            indicator="macd",
            curr_date=curr_date,
            look_back_days=look_back_days,
            online=True
        )
        print(result)
    except Exception as e:
        print(f"Error getting MACD indicator (online): {e}")
    
    print("\n" + "="*80 + "\n")
    
    # Example 4: Get Bollinger Bands indicator (online mode)
    print("--- Example 4: Bollinger Bands Indicator (Online Mode) ---")
    try:
        result = get_stock_stats_indicators_window(
            symbol=symbol,
            indicator="boll",
            curr_date=curr_date,
            look_back_days=look_back_days,
            online=True
        )
        print(result)
    except Exception as e:
        print(f"Error getting Bollinger Bands indicator (online): {e}")
    
    print("\n" + "="*80 + "\n")
    
    # Example 5: Get volume-based indicator (online mode)
    print("--- Example 5: Volume-Based Indicator (Online Mode) ---")
    try:
        result = get_stock_stats_indicators_window(
            symbol=symbol,
            indicator="mfi",
            curr_date=curr_date,
            look_back_days=look_back_days,
            online=True
        )
        print(result)
    except Exception as e:
        print(f"Error getting MFI indicator (online): {e}")
    
    print("\n" + "="*80 + "\n")
    
    # Example 6: Demonstrate different look-back periods
    print("--- Example 6: Different Look-Back Periods ---")
    look_back_periods = [7, 14, 30, 60]
    
    for period in look_back_periods:
        print(f"\n--- {period} Days Look-Back ---")
        try:
            result = get_stock_stats_indicators_window(
                symbol=symbol,
                indicator="rsi",
                curr_date=curr_date,
                look_back_days=period,
                online=True
            )
            # Print just the first few lines to avoid overwhelming output
            lines = result.split('\n')
            print('\n'.join(lines[:10]) + "\n...")
        except Exception as e:
            print(f"Error with {period} days look-back: {e}")
    
    print("\n" + "="*80 + "\n")
    
    # Example 7: Try different symbols
    print("--- Example 7: Different Stock Symbols ---")
    symbols_to_try = ["TSLA", "MSFT", "GOOGL"]
    
    for sym in symbols_to_try:
        print(f"\n--- {sym} RSI Analysis ---")
        try:
            result = get_stock_stats_indicators_window(
                symbol=sym,
                indicator="rsi",
                curr_date=curr_date,
                look_back_days=14,
                online=True
            )
            # Print just the first few lines
            lines = result.split('\n')
            print('\n'.join(lines[:8]) + "\n...")
        except Exception as e:
            print(f"Error getting {sym} RSI: {e}")
    
    print("\n" + "="*80 + "\n")
    
    # Summary of available indicators
    print("--- Available Technical Indicators ---")
    print("The following indicators are supported:")
    for i, indicator in enumerate(indicators, 1):
        print(f"{i:2d}. {indicator}")
    
    print(f"\nTotal: {len(indicators)} indicators")
    print("\nNote: Each indicator provides specific technical analysis insights:")
    print("- Moving Averages: Trend direction and support/resistance")
    print("- MACD: Momentum and trend changes")
    print("- RSI: Overbought/oversold conditions")
    print("- Bollinger Bands: Volatility and breakout signals")
    print("- Volume Indicators: Price-volume relationship confirmation")

if __name__ == "__main__":
    main() 