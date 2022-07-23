# Module 1

## 1.1 Basics
We write the code line by line. From left to right, top to bottom.

### Zen of Python
Python's design philosophy:

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

A variable is a small object that Python understands:
```python
greetings = "Hello, world"
print(greetings)
```
The word greetings is a variable here. Using the equals sign (=) we have assigned the string `"Hello, world"` to it. Now, if we call this variable by print(greetings), its contents, i.e. the text Hello, world, will appear on the screen.

Variables are like boxes into which we put some content. In this case it's a string, but we can also put in other data, e.g. numbers.

More precisely, variables are places in the computer's memory where we store some data. We could tell the machine: I need the information you are holding at address 0x100200, but such a memory reference would be cumbersome. This is why variables were invented, which can be named in a language we can understand.

### Reserved Keywords 
There are several words in the language that are reserved for other purposes, such as the word `for` or `if`. Variables must not be named in this way to avoid confusion. 

There are more such reserved phrases: https://docs.python.org/3/reference/lexical_analysis.html#keywords


### Naming rules

There are a few variable naming rules that you must follow:

* the name of a variable must start with either a letter or an underscore,
* numbers may only occur after the first character,
* variables are case-sensitive, e.g. `myGreetings` and `mygreetings` are two different variables.

Here are examples of bad names:
* 1variable (no!)
* variable with spaces (never!)
* variable& (yuck!)

In contrast, these are good names:
* variable1
* variable_with_underscores


### Naming conventions

It is useful to follow certain conventions - agreements that help to write code so that it is easy to read regardless of place. So there are guidelines for how we should name variables, functions or classes, the use of tabs instead of spaces is discussed, and so on. 

Many conventions are described in the official PEP8 document (Style Guide): https://peps.python.org/pep-0008/ 

You can also browse an abbreviated description of the most important rules on the official Python website: https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style

### Data types

#### Strings
A string is created by enclosing the text in single quotes or double quotes:
```python
    print('Hello, world')
    print("Hi")
```
There are no rigid rules but:
* for texts that are a short category/symbol (most often: one word) it is best to use double quotes,
* for texts that are longer and are some kind of narrative (most often: many words) use single quotes.

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