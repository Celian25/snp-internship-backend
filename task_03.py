from typing import Union

def max_odd(array: list) -> Union[int, None]:
    odd_numbers = list(filter(lambda el: el%2 != 0 , array))
    return max(odd_numbers) if odd_numbers else None

print(max_odd([24.0,2,6,4,4]))