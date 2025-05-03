def connect_dicts(dict1: dict, dict2: dict) -> dict:
    count1 = sum(dict1.values())
    count2 = sum(dict2.values())

    priority = (count2, count1) if count2 > count1 or count2 == count1 else (count1, count2)

    result = {}

    if priority == (count2, count1):
        for key, val in dict1.items():
            if val >= 10 and key not in dict2:
                result[key] = val

        for key, val in dict2.items():
            if val >= 10:
                result[key] = val

        sorted_result = {key: val for key, val in sorted(result.items(), key=lambda item: item[1])}
    else:
        for key, val in dict2.items():
            if val >= 10 and key not in dict1:
                result[key] = val

        for key, val in dict1.items():
            if val >= 10:
                result[key] = val

        sorted_result = {key: val for key, val in sorted(result.items(), key=lambda item: item[1])}

    return sorted_result


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
