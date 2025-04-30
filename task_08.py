from typing import Union


def multiply_numbers(inputs) -> Union[int, None]:
    if type(inputs) is not list:
        inputs = str(inputs)
        numbers = inputs.split()
        for i, val in enumerate(numbers):
            if type(val) is not int:
                continue
            else:
                val = int(val)
                numbers[i] = val
