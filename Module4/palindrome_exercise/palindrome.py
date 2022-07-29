def is_palindrome(text: str) -> bool:
    '''Function checks if a string is a palindrome'''

    if len(text) == 1:
        return False

    last_index = len(text) - 1

    for index, letter in enumerate(text):
        if letter != text[last_index - index]:
            return False

    return True