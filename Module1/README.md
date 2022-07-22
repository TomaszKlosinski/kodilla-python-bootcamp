# Module 1

## 1.1 Basics
We write the code line by line. From left to right, top to bottom.

### Zen of Python
Python design/style guideline:

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!`

### Code Block
Python is famous for its simple syntax. One of its essential elements is a block which is created with indentation (4 spaces).

For example, here are two print messages inside for-loop block:
```python
    for i in range(5):
        print("spam")
        print("eggs")
```

Since both print("spam") and print("eggs") are preceded by four spaces, they belong to a for loop block.

### Comments
Python executes code line by line. Sometimes, however, we may want to include text in the program that we want the interpreter to skip. For that we need a comment. 

For example, we want to leave a comment to other developers:
```python
print("The names of the members of the Monty Python group are:")
# unfortunately I can't remember them all, I have to add the last one
print("John, Michael, Graham, Terry, the other Terry and ...")
```

There are also multi-line comments. We use triple double quotes (`"""`) to place them in the code. 

Here is an example:
```python
print("Day")
"""
what it is
Everyone can see,
but nevertheless
"""
print("good!")
```

A comment might be a valuable information for others and for you in the future - after all, we change code and we may forget something. 

The most important thing, however, is that comments should be rare. We are supposed to write code so that it is understandable and self-explanatory.


## 1.2 Variables
TODO

### Keywords 

### Conventions

### Type

### Strings formatting

### f-Strings

## 1.3 Numbers & operations

### Integers

### Floating point numbers

### Arithmetic operations

## 1.4 Loops

### Nested loops

### Loop control

## 1.5 Conditional expressions and booleans

### if-else

### if-elif-else

## 1.6 More loops

### while

### break, continue, pass