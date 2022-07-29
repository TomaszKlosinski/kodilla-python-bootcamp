def is_palindrome(text: str) -> bool:
    '''Fundtions checks if a string is a palindrome'''

    last_index = len(text) - 1

    for index, letter in enumerate(text):
        if len(text) == 1 or letter != text[last_index - index]:
            return False

    return True