#!/usr/bin/env python3
import redis
import requests
import functools

# Initialize Redis client
redis_client = redis.Redis()

def track_access_count(method):
    """Decorator to track the number of accesses for a URL"""
    @functools.wraps(method)
    def wrapper(url):
        """Wrapper function to increment access count and call the original method"""
        url_count_key = f"count:{url}"
        redis_client.incr(url_count_key)
        return method(url)
    return wrapper

def cache_with_expiry(method):
    """Decorator to cache the result with expiration time of 10 seconds"""
    @functools.wraps(method)
    def wrapper(url):
        """Wrapper function to fetch or cache the HTML content"""
        cached_html = redis_client.get(url)
        if cached_html:
            return cached_html.decode('utf-8')

        html_content = method(url)
        redis_client.setex(url, 10, html_content)
        return html_content
    return wrapper

@track_access_count
@cache_with_expiry
def get_page(url: str) -> str:
    """Retrieve HTML content of a URL using requests"""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Unable to fetch URL {url}, Status code: {response.status_code}"

if __name__ == "__main__":
    # Example usage:
    test_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    print(get_page(test_url))  # First call, should fetch and cache the content
    print(get_page(test_url))  # Second call, should retrieve cached content
