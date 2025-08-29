
# 参数说明：

# top:int，显示最新消息的条数，默认为80条
# show_content:boolean,是否显示新闻内容，默认False
# 返回值说明：

# classify :新闻类别
# title :新闻标题
# time :发布时间
# url :新闻链接
# content:新闻内容（在show_content为True的情况下出现）
# 调用方法：

import os
import tushare as ts
from typing import Optional
import dotenv

dotenv.load_dotenv()

ts.set_token(os.getenv("TUSHARE_TOKEN"))

def print_divider(title):
    print("\n" + "=" * 20 + f" {title} " + "=" * 20)


def safe_head(df: Optional[object], n: int = 5):
    if df is None:
        print("Result is None. This may indicate a network issue, missing token, or a deprecated API.")
        return
    if hasattr(df, "empty") and getattr(df, "empty"):
        print("Empty result.")
        return
    if hasattr(df, "head"):
        try:
            print(df.head(n))
        except Exception as exc:
            print(f"Failed to print head(): {exc}")
    else:
        print(df)


def demo_latest_news():
    print_divider("Latest News - basic")
    try:
        df = ts.get_latest_news()  # 默认最近80条（旧接口，可能返回 None）
        safe_head(df)
    except Exception as exc:
        print(f"get_latest_news() failed: {exc}")

    print_divider("Latest News - top=5, show_content=True")
    try:
        df2 = ts.get_latest_news(top=5, show_content=True)
        if df2 is None:
            print("get_latest_news(top=5, show_content=True) returned None. If you are using the newer Tushare Pro, consider using pro API endpoints instead.")
        else:
            for _, row in df2.iterrows():
                try:
                    classify = row.get("classify", "?") if hasattr(row, "get") else row["classify"]
                    time_ = row.get("time", "?") if hasattr(row, "get") else row["time"]
                    title = row.get("title", "") if hasattr(row, "get") else row["title"]
                    print(f"[{classify}] {time_} - {title}")
                    content = row.get("content") if hasattr(row, "get") else row.get("content")
                    if isinstance(content, str) and content.strip():
                        print(content)
                    url = row.get("url") if hasattr(row, "get") else row["url"]
                    print(url)
                    print("-" * 60)
                except Exception as row_exc:
                    print(f"Failed to print a news row: {row_exc}")
    except Exception as exc:
        print(f"get_latest_news(top=5, show_content=True) failed: {exc}")


# code:股票代码
# date:信息公布日期（YYYY-MM-DD）
# 返回值说明：

# title:信息标题
# type:信息类型
# date:公告日期
# url:信息内容URL
# 调用方法：

def demo_notices():
    print_divider("Notices - default call")
    try:
        df = ts.get_notices()
        safe_head(df)
    except Exception as exc:
        print(f"get_notices() failed: {exc}")

    print_divider("Notices - by code and date")
    try:
        # 示例：浦发银行，示例日期可根据需要调整
        df2 = ts.get_notices(code="600000", date="2020-01-01")
        safe_head(df2)
    except Exception as exc:
        print(f"get_notices(code=..., date=...) failed: {exc}")


if __name__ == "__main__":
    # 可选：设置 Tushare Token（若设置了环境变量 TUSHARE_TOKEN 则自动使用）
    token = os.getenv("TUSHARE_TOKEN")
    if token:
        ts.set_token(token)
        print("Tushare token detected from TUSHARE_TOKEN and configured.")
    else:
        print("No Tushare token found in TUSHARE_TOKEN. Some endpoints may require a token or may be deprecated in free API.")
        print("If you have a token, export it: export TUSHARE_TOKEN=your_token_here")

    demo_latest_news()
    demo_notices()