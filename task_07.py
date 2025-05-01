def combine_anagrams(words_array: list) -> list:
    anagrams = {}
    for word in words_array:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append([word])
    return list(anagrams.values())


print(
    combine_anagrams(
        ["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]
    )
)
