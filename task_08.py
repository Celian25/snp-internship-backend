from typing import Union


def multiply_numbers(inputs: Union[str, float, list, None]) -> Union[int, None]:
    if inputs is None:
        return None
    elements = str(inputs)
    numbers = []

    for el in elements:
        if el.isdigit():
            numbers.append(int(el))

    if len(numbers) == 0:
        return None

    buff = 1
    for num in numbers:
        buff *= num
    return buff


print(multiply_numbers([5, 6, 4]))
