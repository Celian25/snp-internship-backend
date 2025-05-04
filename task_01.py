def is_palindrome(string) -> bool:
    if string is None:
        return False
    s = ""
    for char in str(string).lower():
        if char.isalnum():
            s += char

    return s == s[::-1]
