def cached(func):
    saved = {}

    def get_data(max_size: int | None = None, seconds: int | None = None):
        if not isinstance(max_size, int):
            max_size = None
        if not isinstance(seconds, int):
            seconds = None

        return max_size, seconds

    def wrapper(*args, **kwargs)