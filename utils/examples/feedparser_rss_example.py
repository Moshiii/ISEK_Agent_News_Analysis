
import feedparser
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
import json
import sys

from utils.crypto_rss_utils import get_crypto_rss_feeds


def main():
    """Main function demonstrating various feedparser usage examples"""
    
    get_crypto_rss_feeds()


if __name__ == "__main__":
    main() 