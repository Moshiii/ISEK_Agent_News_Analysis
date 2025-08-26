from pydantic import BaseModel
import os
from openai import OpenAI
import dotenv
from utils.interface import get_YFin_data_online, get_stock_stats_indicators_window
from typing import Annotated
from agents import Agent, function_tool

dotenv.load_dotenv()


@function_tool
def get_YFin_data_online_tool(
    symbol: Annotated[str, "ticker symbol of the company"],
    start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "End date in yyyy-mm-dd format"],
):
    print(f"DEBUG: get_YFin_data_online called with symbol: {symbol}, start_date: {start_date}, end_date: {end_date}")
    return get_YFin_data_online(symbol, start_date, end_date)

@function_tool
def get_stock_stats_indicators_window_tool(
    symbol: Annotated[str, "ticker symbol of the company"],
    indicator: Annotated[str, "technical indicator to get the analysis and report of"],
    curr_date: Annotated[str, "The current trading date you are trading on, YYYY-mm-dd"],
    look_back_days: Annotated[int, "how many days to look back"],
):
    print(f"DEBUG: get_stock_stats_indicators_window called with symbol: {symbol}, indicator: {indicator}, curr_date: {curr_date}, look_back_days: {look_back_days}")
    return get_stock_stats_indicators_window(symbol, indicator, curr_date, look_back_days)

# News analysis agent focused on analyzing recent news and trends
NEWS_PROMPT = (
    "You are a news researcher tasked with analyzing recent news and trends over the past week. Please write a comprehensive report of the current state of the world that is relevant for trading and macroeconomics. Look at news from EODHD, and finnhub to be comprehensive. Do not simply state the trends are mixed, provide detailed and finegrained analysis and insights that may help traders make decisions."
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
    tools=[get_YFin_data_online_tool, get_stock_stats_indicators_window_tool]
) 