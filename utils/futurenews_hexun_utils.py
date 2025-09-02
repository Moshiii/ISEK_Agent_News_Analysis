import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from requests.adapters import HTTPAdapter, Retry

URL = "https://futures.hexun.com/integratednews/index.html"

def make_session():
    """Create a requests session with retry logic and proper headers."""
    s = requests.Session()
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    })
    retries = Retry(total=3, backoff_factor=0.5, status_forcelist=(429, 500, 502, 503, 504))
    s.mount("http://", HTTPAdapter(max_retries=retries))
    s.mount("https://", HTTPAdapter(max_retries=retries))
    return s

def fetch_html(url: str) -> str:
    """Fetch HTML content from a URL with proper encoding handling."""
    with make_session() as s:
        r = s.get(url, timeout=15)
        # Hexun pages often use GB encodings; gb18030 is a superset and safe.
        r.encoding = r.apparent_encoding or "gb18030"
        if not r.encoding or "utf" not in r.encoding.lower():
            r.encoding = "gb18030"
        return r.text

def extract_items(html: str, base_url: str):
    """Extract news items from HTML content."""
    soup = BeautifulSoup(html, "lxml")
    items = []

    # Prefer the known container if present
    container = soup.find("div", class_="temp01")
    anchors = (container.select("li a[href]") if container else soup.select("li a[href]"))

    seen = set()
    for a in anchors:
        title = a.get_text(strip=True)
        href = a.get("href", "").strip()
        if not title or not href or href.lower().startswith("javascript"):
            continue
        url = urljoin(base_url, href)
        key = (title, url)
        if key in seen:
            continue
        seen.add(key)
        items.append({"title": title, "url": url})

    return items

def hexun_news(query: str = "") -> list:
    """Fetch and extract news items from Hexun futures."""
    html = fetch_html(URL)
    items = extract_items(html, URL)
    if query:
        items = [item for item in items if query.lower() in item["title"].lower()]

    return [item["title"] for item in items]

def main():
    """Main execution function."""
    print("Fetching news from Hexun futures...")
    
    try:
        html = fetch_html(URL)
        items = extract_items(html, URL)
        titles = [item["title"] for item in items]
        print(titles)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 
    
