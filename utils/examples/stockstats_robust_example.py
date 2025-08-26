from pathlib import Path
import sys
import os
import dotenv
import time
from datetime import datetime, timedelta

# Ensure project root is on sys.path so `utils` can be imported when running directly
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.interface import get_stock_stats_indicators_window

# Load environment variables from .env
dotenv.load_dotenv()

def robust_indicator_fetch(symbol, indicator, curr_date, look_back_days, max_retries=3, delay=2):
    """
    Robustly fetch indicator data with retry logic and error handling
    """
    for attempt in range(max_retries):
        try:
            print(f"  Attempt {attempt + 1}/{max_retries} for {symbol} {indicator}...")
            
            result = get_stock_stats_indicators_window(
                symbol=symbol,
                indicator=indicator,
                curr_date=curr_date,
                look_back_days=look_back_days,
                online=True
            )
            
            print(f"  ✓ Successfully fetched {indicator} for {symbol}")
            return result, None
            
        except Exception as e:
            error_msg = str(e)
            print(f"  ✗ Attempt {attempt + 1} failed: {error_msg}")
            
            # Check if it's a network-related error
            if any(keyword in error_msg.lower() for keyword in ['connection', 'curl', 'timeout', 'reset', 'network']):
                if attempt < max_retries - 1:
                    print(f"  ⏳ Network error detected. Waiting {delay} seconds before retry...")
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
                else:
                    print(f"  ❌ Max retries reached for {symbol} {indicator}")
                    return None, f"Network error after {max_retries} attempts: {error_msg}"
            else:
                # Non-network error, don't retry
                print(f"  ❌ Non-network error for {symbol} {indicator}: {error_msg}")
                return None, error_msg
    
    return None, "Max retries exceeded"

def test_basic_functionality():
    """
    Test basic functionality with a single stock and indicator
    """
    print("=== Testing Basic Functionality ===\n")
    
    symbol = "AAPL"
    curr_date = "2024-03-01"
    look_back_days = 7
    
    print(f"Testing {symbol} RSI indicator:")
    print(f"  Date: {curr_date}")
    print(f"  Look back: {look_back_days} days")
    print(f"  Mode: Online\n")
    
    result, error = robust_indicator_fetch(symbol, "rsi", curr_date, look_back_days)
    
    if result:
        print("✓ Basic functionality test passed!")
        print("Sample output:")
        lines = result.split('\n')[:8]
        for line in lines:
            print(f"  {line}")
        if len(result.split('\n')) > 8:
            print("  ...")
        return True
    else:
        print(f"✗ Basic functionality test failed: {error}")
        return False

def test_multiple_indicators():
    """
    Test multiple indicators for the same stock
    """
    print("\n=== Testing Multiple Indicators ===\n")
    
    symbol = "AAPL"
    curr_date = "2024-03-01"
    look_back_days = 14
    
    # Test a subset of indicators to avoid overwhelming the API
    indicators_to_test = ["rsi", "close_50_sma", "macd"]
    
    print(f"Testing {len(indicators_to_test)} indicators for {symbol}:")
    print(f"  Date: {curr_date}")
    print(f"  Look back: {look_back_days} days\n")
    
    successful_indicators = []
    failed_indicators = []
    
    for indicator in indicators_to_test:
        print(f"Testing {indicator}...")
        result, error = robust_indicator_fetch(symbol, indicator, curr_date, look_back_days)
        
        if result:
            successful_indicators.append(indicator)
            print(f"  ✓ {indicator}: Success")
        else:
            failed_indicators.append(indicator)
            print(f"  ✗ {indicator}: {error}")
        
        # Small delay between requests to be respectful to the API
        time.sleep(1)
    
    print(f"\nResults: {len(successful_indicators)}/{len(indicators_to_test)} indicators successful")
    
    if successful_indicators:
        print("Successful indicators:", ", ".join(successful_indicators))
    if failed_indicators:
        print("Failed indicators:", ", ".join(failed_indicators))
    
    return len(successful_indicators) > 0

def test_offline_mode():
    """
    Test offline mode (requires local data files)
    """
    print("\n=== Testing Offline Mode ===\n")
    
    symbol = "AAPL"
    curr_date = "2024-03-01"
    look_back_days = 7
    
    print(f"Testing offline mode for {symbol}:")
    print(f"  Date: {curr_date}")
    print(f"  Look back: {look_back_days} days")
    print("  Note: This requires local data files to be present\n")
    
    try:
        result = get_stock_stats_indicators_window(
            symbol=symbol,
            indicator="rsi",
            curr_date=curr_date,
            look_back_days=look_back_days,
            online=False
        )
        print("✓ Offline mode test passed!")
        print("Sample output:")
        lines = result.split('\n')[:8]
        for line in lines:
            print(f"  {line}")
        if len(result.split('\n')) > 8:
            print("  ...")
        return True
        
    except Exception as e:
        print(f"✗ Offline mode test failed: {e}")
        print("This is expected if local data files are not available")
        return False

def test_error_handling():
    """
    Test error handling with invalid parameters
    """
    print("\n=== Testing Error Handling ===\n")
    
    # Test with invalid indicator
    print("Testing invalid indicator...")
    try:
        result = get_stock_stats_indicators_window(
            symbol="AAPL",
            indicator="invalid_indicator",
            curr_date="2024-03-01",
            look_back_days=7,
            online=True
        )
        print("✗ Should have raised an error for invalid indicator")
        return False
    except ValueError as e:
        print(f"✓ Correctly caught invalid indicator error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error type for invalid indicator: {e}")
        return False
    
    # Test with invalid date format
    print("\nTesting invalid date format...")
    try:
        result = get_stock_stats_indicators_window(
            symbol="AAPL",
            indicator="rsi",
            curr_date="invalid-date",
            look_back_days=7,
            online=True
        )
        print("✗ Should have raised an error for invalid date")
        return False
    except Exception as e:
        print(f"✓ Correctly caught invalid date error: {e}")
    
    print("\n✓ Error handling tests passed!")
    return True

def main():
    """
    Main function to run all tests
    """
    print("=== Robust Stock Stats Indicators Testing ===\n")
    print("This script tests the get_stock_stats_indicators_window function")
    print("with comprehensive error handling and retry logic.\n")
    
    tests = [
        ("Basic Functionality", test_basic_functionality),
        ("Multiple Indicators", test_multiple_indicators),
        ("Offline Mode", test_offline_mode),
        ("Error Handling", test_error_handling),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"Running: {test_name}")
        print("-" * 50)
        
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"✗ Test '{test_name}' crashed with error: {e}")
            results.append((test_name, False))
        
        print("\n" + "=" * 80 + "\n")
    
    # Summary
    print("=== Test Summary ===")
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for test_name, success in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The function is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 