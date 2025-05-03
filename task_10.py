def count_words(string: str) -> dict:
    result = {}
    arr = string.lower().replace(",", "").replace("-", "").split()

    for el in arr:
        if el not in result:
            result[el] = 1
        else:
            result[el] += 1
    return result


print(count_words("DOO bee Doo bEE doO"))
