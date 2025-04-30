def sort_list(array: list) -> list:
    if not array:
        return []
    else:
        minimum = min(array)
        maximum = max(array)
        for i, el in enumerate(array):
            if el == minimum:
                array[i] = maximum
            elif el == maximum:
                array[i] = minimum
        return array + [minimum]
