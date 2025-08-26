import finnhub
import os
import dotenv   

dotenv.load_dotenv()
# Setup client
finnhub_client = finnhub.Client(api_key=os.getenv("FINHUB_API_KEY"))

# Basic financials
try:
    res = finnhub_client.company_basic_financials('AAPL', 'all')
    print("company_basic_financials: ok")
except Exception as e:
    print(f"Error getting basic financials: {e}")

# Earnings surprises
try:
    res = finnhub_client.company_earnings('TSLA', limit=5)
    print("company_earnings: ok")
except Exception as e:
    print(f"Error getting company earnings: {e}")

# Company News
# Need to use _from instead of from to avoid conflict
try:
    res = finnhub_client.company_news('AAPL', _from="2020-06-01", to="2020-06-10")
    print("company_news: ok")
except Exception as e:
    print(f"Error getting company news: {e}")

# Company Peers
try:
    res = finnhub_client.company_peers('AAPL')
    print("company_peers: ok")
except Exception as e:
    print(f"Error getting company peers: {e}")

# Company Profile 2
try:
    res = finnhub_client.company_profile2(symbol='AAPL')
    print("company_profile2: ok")
except Exception as e:
    print(f"Error getting company profile 2: {e}")

# List country
try:
    res = finnhub_client.country()
    print("country: ok")
except Exception as e:
    print(f"Error getting country list: {e}")

# Crypto Exchange
try:
    res = finnhub_client.crypto_exchanges()
    print("crypto_exchanges: ok")
except Exception as e:
    print(f"Error getting crypto exchanges: {e}")

# Crypto symbols
try:
    res = finnhub_client.crypto_symbols('BINANCE')
    print("crypto_symbols: ok")
except Exception as e:
    print(f"Error getting crypto symbols: {e}")

# Filings
try:
    res = finnhub_client.filings(symbol='AAPL', _from="2020-01-01", to="2020-06-11")
    print("filings: ok")
except Exception as e:
    print(f"Error getting filings: {e}")

# Financials as reported
try:
    res = finnhub_client.financials_reported(symbol='AAPL', freq='annual')
    print("financials_reported: ok")
except Exception as e:
    print(f"Error getting financials reported: {e}")

# Forex exchanges
try:
    res = finnhub_client.forex_exchanges()
    print("forex_exchanges: ok")
except Exception as e:
    print(f"Error getting forex exchanges: {e}")

# Forex symbols
try:
    res = finnhub_client.forex_symbols('OANDA')
    print("forex_symbols: ok")
except Exception as e:
    print(f"Error getting forex symbols: {e}")

# General news
try:
    res = finnhub_client.general_news('forex', min_id=0)
    print("general_news: ok")
except Exception as e:
    print(f"Error getting general news: {e}")

# IPO calendar
try:
    res = finnhub_client.ipo_calendar(_from="2020-05-01", to="2020-06-01")
    print("ipo_calendar: ok")
except Exception as e:
    print(f"Error getting IPO calendar: {e}")

# Quote
try:
    res = finnhub_client.quote('AAPL')
    print("quote: ok")
except Exception as e:
    print(f"Error getting quote: {e}")

# Recommendation trends
try:
    res = finnhub_client.recommendation_trends('AAPL')
    print("recommendation_trends: ok")
except Exception as e:
    print(f"Error getting recommendation trends: {e}")

# Stock symbols
try:
    res = finnhub_client.stock_symbols('US')[0:5]
    print("stock_symbols: ok")
except Exception as e:
    print(f"Error getting stock symbols: {e}")

# Earnings Calendar
try:
    res = finnhub_client.earnings_calendar(_from="2020-06-10", to="2020-06-30", symbol="", international=False)
    print("earnings_calendar: ok")
except Exception as e:
    print(f"Error getting earnings calendar: {e}")

# Covid-19
try:
    res = finnhub_client.covid19()
    print("covid19: ok")
except Exception as e:
    print(f"Error getting COVID-19 data: {e}")

# FDA Calendar
try:
    res = finnhub_client.fda_calendar()
    print("fda_calendar: ok")
except Exception as e:
    print(f"Error getting FDA calendar: {e}")

# Symbol lookup
try:
    res = finnhub_client.symbol_lookup('apple')
    print("symbol_lookup: ok")
except Exception as e:
    print(f"Error getting symbol lookup: {e}")

# Insider transactions
try:
    res = finnhub_client.stock_insider_transactions('AAPL', '2021-01-01', '2021-03-01')
    print("stock_insider_transactions: ok")
except Exception as e:
    print(f"Error getting insider transactions: {e}")

# Visa application
try:
    res = finnhub_client.stock_visa_application("AAPL", "2021-01-01", "2022-06-15")
    print("stock_visa_application: ok")
except Exception as e:
    print(f"Error getting visa application: {e}")

# Insider sentiment
try:
    res = finnhub_client.stock_insider_sentiment('AAPL', '2021-01-01', '2022-03-01')
    print("stock_insider_sentiment: ok")
except Exception as e:
    print(f"Error getting insider sentiment: {e}")

# Lobbying
try:
    res = finnhub_client.stock_lobbying("AAPL", "2021-01-01", "2022-06-15")
    print("stock_lobbying: ok")
except Exception as e:
    print(f"Error getting lobbying data: {e}")

# USA Spending
try:
    res = finnhub_client.stock_usa_spending("LMT", "2021-01-01", "2022-06-15")
    print("stock_usa_spending: ok")
except Exception as e:
    print(f"Error getting USA spending: {e}")

# Market Holday / Status
try:
    res = finnhub_client.market_holiday(exchange='US')
    print("market_holiday: ok")
except Exception as e:
    print(f"Error getting market holiday: {e}")

try:
    res = finnhub_client.market_status(exchange='US')
    print("market_status: ok")
except Exception as e:
    print(f"Error getting market status: {e}")

print("\nAll working APIs have been tested successfully!") 