#!/usr/bin/env python3
import redis
import requests
from typing import Callable

redis_client = redis.Redis()

def count_requests(method: Callable) -> Callable:
    """Decorator to count the number of requests to a URL"""
    @functools.wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function to increment the count and call the original method"""
        redis_client.incr(f"count:{url}")
        return method(url)
    return wrapper

@count_requests
def get_page(url: str) -> str:
    """Retrieve the HTML content of a URL and cache it with an expiration time"""
    response = requests.get(url)
    redis_client.setex(url, 10, response.text)
    return response.text

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(redis_client.get(f"count:{url}"))
    print(redis_client.get(url))
