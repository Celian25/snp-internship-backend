def coincidence(lst: list = [], rng=None) -> list:
    if not lst or not rng:
        return []
    else:
        rng = list(rng)
        new_lst = [i for i in lst if isinstance(i, (int, float))]
        start = rng[0]
        end = rng[-1]
        return list(filter(lambda el: start <= el <= end, new_lst))


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence([None, 1, "foo", 4, 2, 2.5], range(1, 4)))
print(coincidence())
