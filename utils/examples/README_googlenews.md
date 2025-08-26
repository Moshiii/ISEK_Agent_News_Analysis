# Google News API Examples

This directory contains comprehensive examples demonstrating how to use the `get_google_news` function from `utils.interface`.

## Overview

The `get_google_news` function allows you to fetch news articles from Google News based on:
- **Query**: Search term or topic
- **Current Date**: Reference date in YYYY-MM-DD format
- **Look Back Days**: Number of days to search backwards from the current date

## Function Signature

```python
def get_google_news(
    query: str,           # Query to search with
    curr_date: str,       # Current date in yyyy-mm-dd format
    look_back_days: int   # How many days to look back
) -> str
```

## Example Files

### 1. `googlenews_simple_example.py`
**Basic usage examples for beginners**

- Simple company news fetching
- Sector news analysis
- Different date range examples
- Query variation demonstrations

**Key Features:**
- Basic error handling
- Multiple query types
- Date range variations
- Easy to understand structure

**Usage:**
```bash
cd utils/examples
python googlenews_simple_example.py
```

### 2. `googlenews_comprehensive_example.py`
**Advanced usage with comprehensive analysis**

- Company news analysis
- Sector analysis
- Market event monitoring
- Batch processing capabilities
- Results caching and file export

**Key Features:**
- Object-oriented design with `GoogleNewsAnalyzer` class
- Comprehensive error handling
- JSON export functionality
- Batch processing with rate limiting
- Detailed result summaries

**Usage:**
```bash
cd utils/examples
python googlenews_comprehensive_example.py
```

### 3. `googlenews_use_cases_example.py`
**Real-world use case scenarios**

- Market sentiment analysis
- Competitor monitoring
- Trend detection
- Earnings analysis
- Sector rotation analysis

**Key Features:**
- Practical business scenarios
- Sentiment analysis algorithms
- Trend intensity calculations
- Competitor comparison
- Sector momentum scoring

**Usage:**
```bash
cd utils/examples
python googlenews_use_cases_example.py
```

## Common Use Cases

### 1. Company News Monitoring
```python
from utils.interface import get_google_news

# Get Apple news from last 7 days
apple_news = get_google_news(
    query="Apple Inc",
    curr_date="2024-03-25",
    look_back_days=7
)
```

### 2. Sector Analysis
```python
# Get technology sector news
tech_news = get_google_news(
    query="technology sector",
    curr_date="2024-03-25",
    look_back_days=5
)
```

### 3. Market Event Tracking
```python
# Track earnings-related news
earnings_news = get_google_news(
    query="earnings season",
    curr_date="2024-03-25",
    look_back_days=14
)
```

## Output Format

The function returns a formatted string with:

```
## [Query] Google News, from [start_date] to [end_date]:

### [Article Title] (source: [Source Name])

[Article Snippet]

### [Article Title] (source: [Source Name])

[Article Snippet]
...
```

## Error Handling

All examples include comprehensive error handling:
- API request failures
- Network connectivity issues
- Invalid date formats
- Empty results

## Rate Limiting

The comprehensive example includes built-in rate limiting:
- 0.5 second delay between requests
- Batch processing capabilities
- Error recovery mechanisms

## Dependencies

Make sure you have the following installed:
```bash
pip install python-dotenv
pip install dateutil
```

## Environment Setup

1. Ensure your `.env` file contains:
   ```
   DATA_DIR=/path/to/your/data/directory
   ```

2. The examples will automatically load environment variables

## Best Practices

1. **Query Optimization**: Use specific, targeted queries for better results
2. **Date Ranges**: Start with shorter ranges (1-7 days) for testing
3. **Error Handling**: Always implement try-catch blocks
4. **Rate Limiting**: Add delays between multiple requests
5. **Caching**: Store results to avoid repeated API calls

## Troubleshooting

### Common Issues:

1. **Import Errors**: Ensure the project root is in your Python path
2. **Date Format**: Use YYYY-MM-DD format for dates
3. **Empty Results**: Try different query terms or date ranges
4. **API Limits**: Implement rate limiting for bulk requests

### Debug Mode:

Add debug prints to see what's happening:
```python
try:
    result = get_google_news(query, curr_date, look_back_days)
    print(f"Query: {query}")
    print(f"Result length: {len(result)}")
    print(f"Articles found: {result.count('###')}")
except Exception as e:
    print(f"Error details: {e}")
    import traceback
    traceback.print_exc()
```

## Contributing

When adding new examples:
1. Follow the existing code structure
2. Include comprehensive error handling
3. Add docstrings and comments
4. Test with various query types
5. Update this README if needed

## License

This code follows the same license as the main project. 