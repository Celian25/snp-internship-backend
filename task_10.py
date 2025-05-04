def count_words(string: str) -> dict:
    result = {}
    sorted_str = ""
    for char in string.lower():
        if char.isalpha():
            sorted_str += char
        if char == " ":
            sorted_str += char

    words = sorted_str.split()

    for el in words:
        if el not in result:
            result[el] = 1
        else:
            result[el] += 1
    return result
