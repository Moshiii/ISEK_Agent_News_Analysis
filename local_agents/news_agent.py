from pydantic import BaseModel
import os
from utils.interface import get_google_news, get_crypto_rss_feeds
from typing import Annotated
from agents import Agent, function_tool
import finnhub
import dotenv

dotenv.load_dotenv()

finnhub_client = finnhub.Client(api_key=os.getenv("FINNHUB_API_KEY"))

@function_tool
def finhub_company_news_tool(
    symbol: Annotated[str, "ticker symbol of the company"],
    start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "End date in yyyy-mm-dd format"],
):
    print(f"DEBUG: finhub_company_news_tool called with symbol: {symbol}, start_date: {start_date}, end_date: {end_date}")
    return finnhub_client.company_news(symbol, _from=start_date, to=end_date)

@function_tool
def get_google_news_tool(
    query: Annotated[str, "Query to search with"],
    curr_date: Annotated[str, "Curr date in yyyy-mm-dd format"],
    look_back_days: Annotated[int, "how many days to look back"],
):
    print(f"DEBUG: get_google_news_tool called with query: {query}, curr_date: {curr_date}, look_back_days: {look_back_days}")
    return get_google_news(query, curr_date, look_back_days)

@function_tool
def get_crypto_rss_feeds_tool(
    ticker: Annotated[str, "ticker symbol of the crypto asset"],
):
    print(f"DEBUG: get_crypto_rss_feeds_tool called with ticker: {ticker}")
    return get_crypto_rss_feeds(ticker)
   



# News analysis agent focused on analyzing recent news and trends
NEWS_PROMPT = (
    "You are a news researcher tasked with analyzing recent news and trends over the past week. Please write a comprehensive report of the current state of the world that is relevant for trading and macroeconomics. Look at news from google news, and finnhub to be comprehensive. Do not simply state the trends are mixed, provide detailed and finegrained analysis and insights that may help traders make decisions."
    + " Make sure to append a Markdown table at the end of the report to organize key points in the report, organized and easy to read."
    + " Based on your analysis, provide a specific recommendation to buy, sell, or hold. End with a firm decision and always conclude your response with 'FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**' to confirm your recommendation."
)


class NewsAnalysisSummary(BaseModel):
    summary: str
    """Short text summary for this aspect of the analysis."""


news_agent = Agent(
    name="NewsResearcherAgent",
    instructions=NEWS_PROMPT,
    model="gpt-4o",
    output_type=NewsAnalysisSummary,
    # tools=[finhub_company_news_tool, get_google_news_tool, get_crypto_rss_feeds_tool]  
    tools=[get_crypto_rss_feeds_tool]  
) 