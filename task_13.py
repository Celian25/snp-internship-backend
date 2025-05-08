from functools import lru_cache, update_wrapper
from math import floor
import time


def cached(max_size: int | None = None, seconds: int | None = None):
    if not isinstance(max_size, int):
        max_size = None
    if not isinstance(seconds, int):
        seconds = None

    def decorator(func):
        @lru_cache(maxsize=max_size)
        def cached_function(cache_time, *args, **kwargs):
            return func(*args, **kwargs)

        def wrapper(*args, **kwargs):
            if seconds is None:
                cache_time = 0
            else:
                cur_time = time.time()
                cache_time = floor(cur_time / seconds) * seconds
            return cached_function(cache_time, *args, **kwargs)

        return update_wrapper(wrapper, func)

    return decorator


@cached(max_size=3, seconds=2)
def slow_function(x):
    print(f"Calculating {x}...")
    return x**x


print(slow_function(2))  # Should print "Calculating 2..." and return 4
print(slow_function(2))  # Should return 4 without printing
time.sleep(3)
print(slow_function(2))
