# Exercise: Palindromes

Your task will be to write a function that checks whether a word is a palindrome. A palindrome is a word that, when read from left to right and right to left, looks the same. Examples include 'ada' or 'kayak'.

Program a function that takes one argument (of type string) and returns a boolean value: True/False, telling whether the given text is a palindrome.

**Hint**: Remember that string/text is a collection of characters. You already know the collection functions that allow you to refer to elements indexed from the beginning and from the end.

## Solution

The function implementing palindrome check is in `palindrome.py` file. 

File `find_all_palindromes.py` is a program that is using above function to find all palindromes in English and Polish dictionaries fetched from the Internet. 

File `test_palindrome_exercise.py` includes tests for `palindrome.py` - to execute them run:
```python
python3 test_palindrome_exercise.py
```
or run (if you have [pytest](https://docs.pytest.org/) installed):
```python
pytest
```
