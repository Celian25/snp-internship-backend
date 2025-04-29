# Вместо list и range использовал lst и rng из-за конфликта с встроенными функциями
def coincidence(lst: list, rng: tuple) -> list:
    if not lst or type(rng) != tuple or len(rng) < 2:
        return []
    else:
        return list(filter(lambda el: rng[0] <= el <= rng[1], lst))
