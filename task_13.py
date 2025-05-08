import time
from functools import lru_cache


def cached(max_size: int | None = None, seconds: int | None = None):
    if not isinstance(max_size, int):
        max_size = None
    if not isinstance(seconds, int):
        seconds = None

    def wrapper(func):
        @lru_cache(maxsize=max_size)
        def inner(__ttl, *args, **kwargs):
            return func(*args, **kwargs)

        def time_wrapper(*args, **kwargs):
            if seconds is None:
                return inner(0, *args, **kwargs)
            return inner(time.time() // seconds, *args, **kwargs)

        return time_wrapper

    return wrapper
