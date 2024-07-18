#!/usr/bin/env python3
"""
web.py - Module for implementing an expiring web cache and tracker using Redis.
"""

import redis
import requests
from typing import Callable

# Initialize Redis client
client = redis.Redis()


def get_page(url: str) -> str:
    """
    Retrieves the HTML content of a given URL and
    caches it in Redis for 10 seconds.
    Also tracks the number of times a particular URL was accessed.

    Args:
        url (str): The URL to retrieve the HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    # Increment the count of URL accesses
    client.incr(f"count:{url}")

    # Check if the URL content is cached
    cached_content = client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    # Fetch the URL content and cache it with an expiration time of 10 seconds
    response = requests.get(url)
    client.setex(url, 10, response.text)

    return response.text


if __name__ == "__main__":
    # Example usage
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    access_count = client.get(f"count:{url}").decode('utf-8')
    print(f"Access count for {url}: {access_count}")
