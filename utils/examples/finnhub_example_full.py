import finnhub
import os
import dotenv   

dotenv.load_dotenv()
# Setup client
finnhub_client = finnhub.Client(api_key=os.getenv("FINHUB_API_KEY"))

# Stock candles
try:
    res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
    print("stock_candles: ok")
except Exception as e:
    print(f"Error getting stock candles: {e}")

# Aggregate Indicators
try:
    res = finnhub_client.aggregate_indicator('AAPL', 'D')
    print("aggregate_indicator: ok")
except Exception as e:
    print(f"Error getting aggregate indicators: {e}")

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

# EPS estimates
try:
    res = finnhub_client.company_eps_estimates('AMZN', freq='quarterly')
    print("company_eps_estimates: ok")
except Exception as e:
    print(f"Error getting EPS estimates: {e}")

# Company Executives
try:
    res = finnhub_client.company_executive('AAPL')
    print("company_executive: ok")
except Exception as e:
    print(f"Error getting company executives: {e}")

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

# Company Profile
try:
    res = finnhub_client.company_profile(symbol='AAPL')
    print("company_profile: ok")
except Exception as e:
    print(f"Error getting company profile by symbol: {e}")

try:
    res = finnhub_client.company_profile(isin='US0378331005')
    print("company_profile: ok")
except Exception as e:
    print(f"Error getting company profile by ISIN: {e}")

try:
    res = finnhub_client.company_profile(cusip='037833100')
    print("company_profile: ok")
except Exception as e:
    print(f"Error getting company profile by CUSIP: {e}")

# Company Profile 2
try:
    res = finnhub_client.company_profile2(symbol='AAPL')
    print("company_profile2: ok")
except Exception as e:
    print(f"Error getting company profile 2: {e}")

# Revenue Estimates
try:
    res = finnhub_client.company_revenue_estimates('TSLA', freq='quarterly')
    print("company_revenue_estimates: ok")
except Exception as e:
    print(f"Error getting revenue estimates: {e}")

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

# Economic data
try:
    res = finnhub_client.economic_data('MA-USA-656880')
    print("economic_data: ok")
except Exception as e:
    print(f"Error getting economic data: {e}")

# Filings
try:
    res = finnhub_client.filings(symbol='AAPL', _from="2020-01-01", to="2020-06-11")
    print("filings: ok")
except Exception as e:
    print(f"Error getting filings: {e}")

# Financials
try:
    res = finnhub_client.financials('AAPL', 'bs', 'annual')
    print("financials: ok")
except Exception as e:
    print(f"Error getting financials: {e}")

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

# Forex all pairs
try:
    res = finnhub_client.forex_rates(base='USD')
    print("forex_rates: ok")
except Exception as e:
    print(f"Error getting forex rates: {e}")

# Forex symbols
try:
    res = finnhub_client.forex_symbols('OANDA')
    print("forex_symbols: ok")
except Exception as e:
    print(f"Error getting forex symbols: {e}")

# Fund Ownership
try:
    res = finnhub_client.fund_ownership('AMZN', limit=5)
    print("fund_ownership: ok")
except Exception as e:
    print(f"Error getting fund ownership: {e}")

# General news
try:
    res = finnhub_client.general_news('forex', min_id=0)
    print("general_news: ok")
except Exception as e:
    print(f"Error getting general news: {e}")

# Investors ownership
try:
    res = finnhub_client.ownership('AAPL', limit=5)
    print("ownership: ok")
except Exception as e:
    print(f"Error getting ownership: {e}")

# IPO calendar
try:
    res = finnhub_client.ipo_calendar(_from="2020-05-01", to="2020-06-01")
    print("ipo_calendar: ok")
except Exception as e:
    print(f"Error getting IPO calendar: {e}")

# Major developments
try:
    res = finnhub_client.press_releases('AAPL', _from="2020-01-01", to="2020-12-31")
    print("press_releases: ok")
except Exception as e:
    print(f"Error getting press releases: {e}")

# News sentiment
try:
    res = finnhub_client.news_sentiment('AAPL')
    print("news_sentiment: ok")
except Exception as e:
    print(f"Error getting news sentiment: {e}")

# Pattern recognition
try:
    res = finnhub_client.pattern_recognition('AAPL', 'D')
    print("pattern_recognition: ok")
except Exception as e:
    print(f"Error getting pattern recognition: {e}")

# Price target
try:
    res = finnhub_client.price_target('AAPL')
    print("price_target: ok")
except Exception as e:
    print(f"Error getting price target: {e}")

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

# Stock dividends
try:
    res = finnhub_client.stock_dividends('KO', _from='2019-01-01', to='2020-01-01')
    print("stock_dividends: ok")
except Exception as e:
    print(f"Error getting stock dividends: {e}")

# Stock dividends 2
try:
    res = finnhub_client.stock_basic_dividends("KO")
    print("stock_basic_dividends: ok")
except Exception as e:
    print(f"Error getting stock basic dividends: {e}")

# Stock symbols
try:
    res = finnhub_client.stock_symbols('US')[0:5]
    print("stock_symbols: ok")
except Exception as e:
    print(f"Error getting stock symbols: {e}")

# Transcripts
try:
    res = finnhub_client.transcripts('AAPL_162777')
    print("transcripts: ok")
except Exception as e:
    print(f"Error getting transcripts: {e}")

# Transcripts list
try:
    res = finnhub_client.transcripts_list('AAPL')
    print("transcripts_list: ok")
except Exception as e:
    print(f"Error getting transcripts list: {e}")

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

# Upgrade downgrade
try:
    res = finnhub_client.upgrade_downgrade(symbol='AAPL', _from='2020-01-01', to='2020-06-30')
    print("upgrade_downgrade: ok")
except Exception as e:
    print(f"Error getting upgrade downgrade: {e}")

# Economic code
try:
    res = finnhub_client.economic_code()[0:5]
    print("economic_code: ok")
except Exception as e:
    print(f"Error getting economic code: {e}")

# Economic calendar
try:
    res = finnhub_client.calendar_economic('2021-01-01', '2021-01-07')
    print("calendar_economic: ok")
except Exception as e:
    print(f"Error getting economic calendar: {e}")

# Support resistance
try:
    res = finnhub_client.support_resistance('AAPL', 'D')
    print("support_resistance: ok")
except Exception as e:
    print(f"Error getting support resistance: {e}")

# Technical Indicator
try:
    res = finnhub_client.technical_indicator(symbol="AAPL", resolution='D', _from=1583098857, to=1584308457, indicator='rsi', indicator_fields={"timeperiod": 3})
    print("technical_indicator: ok")
except Exception as e:
    print(f"Error getting technical indicator: {e}")

# Stock splits
try:
    res = finnhub_client.stock_splits('AAPL', _from='2000-01-01', to='2020-01-01')
    print("stock_splits: ok")
except Exception as e:
    print(f"Error getting stock splits: {e}")

# Forex candles
try:
    res = finnhub_client.forex_candles('OANDA:EUR_USD', 'D', 1590988249, 1591852249)
    print("forex_candles: ok")
except Exception as e:
    print(f"Error getting forex candles: {e}")

# Crypto Candles
try:
    res = finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'D', 1590988249, 1591852249)
    print("crypto_candles: ok")
except Exception as e:
    print(f"Error getting crypto candles: {e}")

# Tick Data
try:
    res = finnhub_client.stock_tick('AAPL', '2020-03-25', 500, 0)
    print("stock_tick: ok")
except Exception as e:
    print(f"Error getting stock tick: {e}")

# BBO Data
try:
    res = finnhub_client.stock_nbbo("AAPL", "2020-03-25", 500, 0)
    print("stock_nbbo: ok")
except Exception as e:
    print(f"Error getting BBO data: {e}")

# Indices Constituents
try:
    res = finnhub_client.indices_const(symbol = "^GSPC")
    print("indices_const: ok")
except Exception as e:
    print(f"Error getting indices constituents: {e}")

# Indices Historical Constituents
try:
    res = finnhub_client.indices_hist_const(symbol = "^GSPC")
    print("indices_hist_const: ok")
except Exception as e:
    print(f"Error getting indices historical constituents: {e}")

# ETFs Profile
try:
    res = finnhub_client.etfs_profile('SPY')
    print("etfs_profile: ok")
except Exception as e:
    print(f"Error getting ETF profile by symbol: {e}")

try:
    res = finnhub_client.etfs_profile(isin="US78462F1030")
    print("etfs_profile: ok")
except Exception as e:
    print(f"Error getting ETF profile by ISIN: {e}")

# ETFs Holdings
try:
    res = finnhub_client.etfs_holdings('SPY')
    print("etfs_holdings: ok")
except Exception as e:
    print(f"Error getting ETF holdings by symbol: {e}")

try:
    res = finnhub_client.etfs_holdings(isin="US00214Q1040", skip=2)
    print("etfs_holdings: ok")
except Exception as e:
    print(f"Error getting ETF holdings by ISIN: {e}")

try:
    res = finnhub_client.etfs_holdings("IPO", date='2022-03-10')
    print("etfs_holdings: ok")
except Exception as e:
    print(f"Error getting ETF holdings by name: {e}")

# ETFs Sector Exposure
try:
    res = finnhub_client.etfs_sector_exp('SPY')
    print("etfs_sector_exp: ok")
except Exception as e:
    print(f"Error getting ETF sector exposure: {e}")

# ETFs Country Exposure
try:
    res = finnhub_client.etfs_country_exp('SPY')
    print("etfs_country_exp: ok")
except Exception as e:
    print(f"Error getting ETF country exposure: {e}")

# International Filings
try:
    res = finnhub_client.international_filings('RY.TO')
    print("international_filings: ok")
except Exception as e:
    print(f"Error getting international filings by symbol: {e}")

try:
    res = finnhub_client.international_filings(country='GB')
    print("international_filings: ok")
except Exception as e:
    print(f"Error getting international filings by country: {e}")

# SEC Sentiment Analysis
try:
    res = finnhub_client.sec_sentiment_analysis('0000320193-20-000052')
    print("sec_sentiment_analysis: ok")
except Exception as e:
    print(f"Error getting SEC sentiment analysis: {e}")

# SEC similarity index
try:
    res = finnhub_client.sec_similarity_index('AAPL')
    print("sec_similarity_index: ok")
except Exception as e:
    print(f"Error getting SEC similarity index: {e}")

# Bid Ask
try:
    res = finnhub_client.last_bid_ask('AAPL')
    print("last_bid_ask: ok")
except Exception as e:
    print(f"Error getting bid ask: {e}")

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

# Mutual Funds Profile
try:
    res = finnhub_client.mutual_fund_profile("VTSAX")
    print("mutual_fund_profile: ok")
except Exception as e:
    print(f"Error getting mutual fund profile by symbol: {e}")

try:
    res = finnhub_client.mutual_fund_profile(isin="US9229087286")
    print("mutual_fund_profile: ok")
except Exception as e:
    print(f"Error getting mutual fund profile by ISIN: {e}")

# Mutual Funds Holdings
try:
    res = finnhub_client.mutual_fund_holdings("VTSAX")
    print("mutual_fund_holdings: ok")
except Exception as e:
    print(f"Error getting mutual fund holdings by symbol: {e}")

try:
    res = finnhub_client.mutual_fund_holdings(isin="US9229087286", skip=2)
    print("mutual_fund_holdings: ok")
except Exception as e:
    print(f"Error getting mutual fund holdings by ISIN: {e}")

# Mutual Funds Sector Exposure
try:
    res = finnhub_client.mutual_fund_sector_exp("VTSAX")
    print("mutual_fund_sector_exp: ok")
except Exception as e:
    print(f"Error getting mutual fund sector exposure: {e}")

# Mutual Funds Country Exposure
try:
    res = finnhub_client.mutual_fund_country_exp("VTSAX")
    print("mutual_fund_country_exp: ok")
except Exception as e:
    print(f"Error getting mutual fund country exposure: {e}")

# Revenue breakdown
try:
    res = finnhub_client.stock_revenue_breakdown('AAPL')
    print("stock_revenue_breakdown: ok")
except Exception as e:
    print(f"Error getting revenue breakdown: {e}")

# Social sentiment
try:
    res = finnhub_client.stock_social_sentiment('GME')
    print("stock_social_sentiment: ok")
except Exception as e:
    print(f"Error getting social sentiment: {e}")

# Investment Themes
try:
    res = finnhub_client.stock_investment_theme('financialExchangesData')
    print("stock_investment_theme: ok")
except Exception as e:
    print(f"Error getting investment themes: {e}")

# Supply chain
try:
    res = finnhub_client.stock_supply_chain('AAPL')
    print("stock_supply_chain: ok")
except Exception as e:
    print(f"Error getting supply chain: {e}")

# Company ESG
try:
    res = finnhub_client.company_esg_score("AAPL")
    print("company_esg_score: ok")
except Exception as e:
    print(f"Error getting company ESG score: {e}")

# Earnings Quality Score
try:
    res = finnhub_client.company_earnings_quality_score('AAPL', 'quarterly')
    print("company_earnings_quality_score: ok")
except Exception as e:
    print(f"Error getting earnings quality score: {e}")

# Crypto Profile
try:
    res = finnhub_client.crypto_profile('BTC')
    print("crypto_profile: ok")
except Exception as e:
    print(f"Error getting crypto profile: {e}")

# EBITDA Estimates
try:
    res = finnhub_client.company_ebitda_estimates("TSLA", freq="quarterly")
    print("company_ebitda_estimates: ok")
except Exception as e:
    print(f"Error getting EBITDA estimates: {e}")

# EBIT Estimates
try:
    res = finnhub_client.company_ebit_estimates("TSLA", freq="quarterly")
    print("company_ebit_estimates: ok")
except Exception as e:
    print(f"Error getting EBIT estimates: {e}")

# USPTO Patent
try:
    res = finnhub_client.stock_uspto_patent("AAPL", "2021-01-01", "2021-12-31")
    print("stock_uspto_patent: ok")
except Exception as e:
    print(f"Error getting USPTO patent: {e}")

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

# Bond Profile
try:
    res = finnhub_client.bond_profile(isin='US912810TD00')
    print("bond_profile: ok")
except Exception as e:
    print(f"Error getting bond profile: {e}")

# Bond price
try:
    res = finnhub_client.bond_price('US912810TD00', 1590988249, 1649099548)
    print("bond_price: ok")
except Exception as e:
    print(f"Error getting bond price: {e}")

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

# Sector metrics
try:
    res = finnhub_client.sector_metric('NA')
    print("sector_metric: ok")
except Exception as e:
    print(f"Error getting sector metrics: {e}")

## Fund's EET data
try:
    res = finnhub_client.mutual_fund_eet('LU2036931686')
    print("mutual_fund_eet: ok")
except Exception as e:
    print(f"Error getting mutual fund EET: {e}")

try:
    res = finnhub_client.mutual_fund_eet_pai('LU2036931686')
    print("mutual_fund_eet_pai: ok")
except Exception as e:
    print(f"Error getting mutual fund EET PAI: {e}")

# Symbol & ISIN change
try:
    res = finnhub_client.isin_change(_from='2022-10-01', to='2022-10-07')
    print("isin_change: ok")
except Exception as e:
    print(f"Error getting ISIN change: {e}")

try:
    res = finnhub_client.symbol_change(_from='2022-10-01', to='2022-10-07')
    print("symbol_change: ok")
except Exception as e:
    print(f"Error getting symbol change: {e}")

# 13-F data
try:
    res = finnhub_client.institutional_profile()
    print("institutional_profile: ok")
except Exception as e:
    print(f"Error getting institutional profile: {e}")

try:
    res = finnhub_client.institutional_portfolio(cik='1000097', _from='2022-01-01', to='2022-10-07')
    print("institutional_portfolio: ok")
except Exception as e:
    print(f"Error getting institutional portfolio: {e}")

try:
    res = finnhub_client.institutional_ownership('TSLA', '', _from='2022-01-01', to='2022-10-07')
    print("institutional_ownership: ok")
except Exception as e:
    print(f"Error getting institutional ownership: {e}")

# Bond yield and FINRA Trace tick
try:
    res = finnhub_client.bond_yield_curve('10y')
    print("bond_yield_curve: ok")
except Exception as e:
    print(f"Error getting bond yield curve: {e}")

try:
    res = finnhub_client.bond_tick('US693475BF18', '2022-08-19', 500, 0, 'trace')
    print("bond_tick: ok")
except Exception as e:
    print(f"Error getting bond tick: {e}")

# Congressional Trading
try:
    res = finnhub_client.congressional_trading('AAPL', '2020-01-01', '2023-03-31')
    print("congressional_trading: ok")
except Exception as e:
    print(f"Error getting congressional trading: {e}")

# Price metrics with historical data
try:
    res = finnhub_client.price_metrics(symbol="AAPL", date="2022-01-01")
    print("price_metrics: ok")
except Exception as e:
    print(f"Error getting price metrics: {e}")

## Market Holday / Status
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

# Bank Branch
try:
    res = finnhub_client.bank_branch("JPM")
    print("bank_branch: ok")
except Exception as e:
    print(f"Error getting bank branch: {e}")
