from functools import lru_cache, update_wrapper
from math import floor
import time


def cached(max_size: int | None = None, seconds: int | None = None):
    if not isinstance(max_size, int):
        max_size = None
    if not isinstance(seconds, int):
        seconds = None

    ttl = seconds if seconds is not None else 65536

    hash_gen = _ttl_hash_gen(ttl)

    def wrapper(func):
        @lru_cache(max_size=max_size)
        def ttl_func(ttl_hash, *args, **kwargs):
            return func(*args, **kwargs)

        def wrapped(*args, **kwargs):
            th = next(hash_gen)
            return ttl_func(th, *args, **kwargs)

        return update_wrapper(wrapped, func)

    return wrapper


def _ttl_hash_gen(seconds: int):
    start_time = time.time()

    while True:
        yield floor((time.time() - start_time) / seconds)
