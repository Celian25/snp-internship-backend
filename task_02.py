def coincidence(lst: list = [], rng=None) -> list:
    if not lst or not rng:
        return []
    else:
        rng = list(rng)
        new_lst = [i for i in lst if isinstance(i, (int, float))]
        start = rng[0]
        end = rng[-1]
        return list(filter(lambda el: start <= el <= end, new_lst))
