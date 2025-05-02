def max_odd(array: list) -> int | None:
    odd_numbers = list(
        filter(
            lambda el: (
                el % 2 != 0
                if type(el) is int or (type(el) is float and el % 1 == 0)
                else False
            ),
            array,
        )
    )
    return int(max(odd_numbers)) if odd_numbers else None


print(max_odd([21.0, 2, 6, 4, 3]))
