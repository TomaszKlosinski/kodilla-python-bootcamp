def is_palindrome(text: str) -> bool:
    """Function checks if a string is a palindrome"""

    return text == text[::-1]
