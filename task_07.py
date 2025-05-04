def combine_anagrams(words_array: list) -> list:
    anagrams = {}
    for word in words_array:
        sorted_word = "".join(sorted(word.lower()))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    return list(anagrams.values())
