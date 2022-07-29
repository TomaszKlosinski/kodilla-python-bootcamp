def is_palindrome(text: str) -> bool:
    last_index = len(text) - 1
    first_half = text[:len(text)//2]

    for index, letter in enumerate(text):
        if len(text) == 1 or letter != text[last_index - index]:
            return False

    return True