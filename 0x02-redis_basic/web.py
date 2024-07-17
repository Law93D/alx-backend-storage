#!/usr/bin/env python3
import redis
import requests

# Initialize Redis client
redis_client = redis.Redis()

def get_page(url: str) -> str:
    """Retrieve HTML content of a URL and cache it with Redis"""
    # Track the number of accesses for the URL
    url_count_key = f"count:{url}"
    redis_client.incr(url_count_key)

    # Check if the URL content is cached in Redis
    cached_html = redis_client.get(url)
    if cached_html:
        return cached_html.decode('utf-8')

    # If not cached, fetch HTML from the URL
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        # Cache HTML content in Redis with expiration of 10 seconds
        redis_client.setex(url, 10, html_content)
        return html_content
    else:
        return f"Error: Unable to fetch URL {url}, Status code: {response.status_code}"

if __name__ == "__main__":
    # Example usage:
    test_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    print(get_page(test_url))  # First call, should fetch and cache the content
    print(get_page(test_url))  # Second call, should retrieve cached content
