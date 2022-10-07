#!/usr/bin/env python3
"""Program to fetch all palindromes in English and Polish"""

from urllib.request import urlopen
from palindrome import is_palindrome


def find_all_paindromes_online(word_site: str) -> list[str]:
    response = urlopen(word_site)
    words = response.read().decode("utf-8").splitlines()

    result = [word for word in words if is_palindrome(word)]

    print(result)


def main() -> None:
    print("All palindromes in English language dictionary:")
    find_all_paindromes_online("https://www.mit.edu/~ecprice/wordlist.10000")

    print("")

    print("All palindromes in Polish language dictionary:")
    find_all_paindromes_online(
        "https://zeroxfiftyone.keybase.pub/WordList%20Collection/words.polish.txt"
    )


if __name__ == "__main__":
    main()
