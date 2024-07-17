#!/usr/bin/env python3
import redis
import uuid
import functools
from typing import Union, Callable, Optional

def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to increment count and call the original method"""
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a particular function"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to store call history and call the original method"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper

def replay(method: Callable):
    """Displays the history of calls of a particular function"""
    cache = method.__self__
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")

class Cache:
    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a randomly generated key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis and apply an optional conversion function"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string from Redis"""
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis"""
        return self.get(key, int)

if __name__ == "__main__":
    cache = Cache()
    
    # Test count_calls functionality
    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))
    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))

    # Test call_history functionality
    s1 = cache.store("first")
    print(s1)
    s2 = cache.store("second")
    print(s2)
    s3 = cache.store("third")
    print(s3)

    replay(cache.store)

    inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

    print("inputs: {}".format(inputs))
    print("outputs: {}".format(outputs))

    # Test get, get_str, get_int functionality
    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

    # Print call history for store method
        replay(cache.store)
