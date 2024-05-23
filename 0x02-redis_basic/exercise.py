#!/usr/bin/env python3
"""A module for using the Redis NoSQL data storage.
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """Represents an object for storing data in a Redis data storage.
    """
    def __init__(self) -> None:
        """Initializes a Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """Retrieve data from Redis
        """
        value = self._redis.get(key)
        return fn(value) if fn is not None else value

    def get_int(self, key: str) -> int:
        """Retrieve integer value from Redis Data Storage
        """
        return self.get(key, lambda x: int(x))

    def get_str(self, key: str) -> str:
        """Retrieve string value from Redis Data Storage
        """
        return self.get(key, lambda d: d.decode("utf-8"))


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
