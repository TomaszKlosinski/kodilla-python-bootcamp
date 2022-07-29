#!/usr/bin/env python3

from urllib.request import urlopen
from palindrome_exercise import is_palindrome


def find_all_paindromes_online(word_site):
    response = urlopen(word_site)
    words = response.read().decode('utf-8').splitlines()

    result = []
    for word in words:
        if is_palindrome(word):
            result.append(word)

    print(result)


print("All palindromes in English language dictionary:")
find_all_paindromes_online("https://www.mit.edu/~ecprice/wordlist.10000")

print("")

print("All palindromes in Polish language dictionary:")
find_all_paindromes_online("https://zeroxfiftyone.keybase.pub/WordList%20Collection/words.polish.txt")
