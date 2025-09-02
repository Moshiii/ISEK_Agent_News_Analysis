import feedparser
import json
from typing import Dict, List, Any


def extract_feed_entries(feed_url: str, max_entries: int = 999) -> List[Dict[str, Any]]:
    try:
        feed = feedparser.parse(feed_url)
        if not feed.entries:
            return []

        entries: List[Dict[str, Any]] = []
        for entry in feed.entries[:max_entries]:
            entry_info = {
                'title': entry.get('title', 'No title'),
                'link': entry.get('link', 'No link'),
                'published': entry.get('published', 'No date'),
                'summary': entry.get('summary', 'No summary'),
            }
            entries.append(entry_info)

        return entries
    except Exception:
        return []


def crypto_rss_feeds(ticker: str = "btc") -> None:
    example_feeds = [
        "https://cointelegraph.com/rss",
        "https://bitcoinist.com/feed/",
        "https://bitcoinethereumnews.com/feed/",
        "https://cryptoverze.com/feed/",
        "https://www.coolwallet.io/blogs/blog.atom",
        "https://latinoreview.com/feed/",
        "https://bitrss.com/rss.xml",
        "https://coinlabz.com/feed/",
        "https://crypto.news/feed/",
        "https://cryptobriefing.com/feed/",
        "https://99bitcoins.com/feed/",
        "https://cryptopotato.com/feed/",
        "https://www.newsbtc.com/feed/",
    ]
    all_entries: List[Dict[str, Any]] = []
    for feed_url in example_feeds:
        entries = extract_feed_entries(feed_url)
        for entry in entries:
            entry_with_source = dict(entry)
            entry_with_source['source'] = feed_url
            all_entries.append(entry_with_source)

    if ticker:
        all_entries = [entry for entry in all_entries if ticker.lower() in entry['title'].lower()]
    return json.dumps(all_entries, indent=2, ensure_ascii=False)