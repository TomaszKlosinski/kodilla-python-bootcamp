# Module 1

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

## 1.1 Basics
We write the code line by line. From left to right, top to bottom.

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

### Variable re-assignment and constants

It is important to remember that once a variable is declared it can be modified many more times. 

Take a look at the following example:
```python
greetings = "Hello, world"
# let me change my mind
greetings = "Hello wonderful world!"
print(greetings)
```

The greetings variable is declared twice here. And what appears on the screen? What was declared last, i.e. `"Hello wonderful world!"`

#### Constants

**NOTE**: In Python there arer no *constants* (i.e. variable-like objects whose values cannot be changed).

There's however a convention to name variables that should not be changed (pseudo-constants) with all capital letters, e.g.:

```python
PI = 3.14
GRAVITY = 9.8
```

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

Many conventions are described in the official PEP8 document (Style Guide): 
https://peps.python.org/pep-0008/ 

You can also browse an abbreviated description of the most important rules on the official Python website: 
https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style

### Data types

Built-in Data Types in Python:
* Binary Types: memoryview, bytearray, bytes
* Boolean Type: bool
* Set Types: frozenset, set
* Mapping Type: dict
* Sequence Types: range, tuple, list
* Numeric Types: complex, float, int
* Text Type: str

#### `type()` function

Let's say we have such string variable:
```python
greetings = "Hello, world"

```
We know that `greetings` is a string because we put the text in quotes.

To confirm that we can use a built-in function called `type()` to check what type a particular piece of data is:
```python
greetings = "Hello, world"
greetings_type = type(greetings)
print(greetings_type)

```

The result you get is `str`, which in Python means string.


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

When we show a greeting on the screen, sometimes we would like to personalise it more. This is where String formatting (kind of templates) come to our aid, which we will populate with the relevant data stored in variables.

For example:
```python
name = "Brian"
personalised_greetings = "Hello %s!" % name
print(personalized_greetings)
```

First we declared a variable that holds a name. Then we created another variable `personalized_greetings`, which is nothing more than another string with `name` variable's value included into it.

It is using a **formater** `%s` in it, and the parameter declaration (`%name`) still appears after double quotes.

The formater `%s` will make a string from variable `name` appear in this place.

The %s formatter is an example of a formatter for text. Of course, there are others, such as `%d`, which is responsible for inserting numbers. 

Let's see how it works and extend our greeting to include the age:
```python
age = 33
name = "Brian"
personalised_greetings = "Hello %s, age %d!" % (name, age)
print(personalized_greetings)
```

The answer we get is:
```python
>> Hello Brian, age 33!
```

Note that when we have more than one parameter (`% (name, age)`), we provide them in brackets.

Look for the other formatters on the official Python website: 
https://docs.python.org/3/library/string.html#format-specification-mini-language

### f-Strings

**NOTE**: f-Strings are a new feature in Python 3.6.

f-Strings allow the user to include a variable's value directly in the string using curly brackets (`{}`).

The previous example using formatter could be re-written with an f-string like this:
```python
age = 33
name = "Brian"
personalised_greetings = f"Hello {name}, age {age}!"
print(personalized_greetings)
```

For the use of the f-string, simply use the letter `f` before the text definition and the previously declared variables in curly brackets.


## 1.3 Numbers & operations

### Integers

Integers are declared like any other variables:
```python
number = 44
print(number)
print(type(number))
```

After typing this code and running the interpreter, we get the following output:
```python
>> 44
>> <class 'int'>
```

First we print the number declared in the variable. However, when we ask for its type, we find out that it is `int` (short for integer).

### Floating point numbers

To declare a float:

```python
my_float = 43.99
print(my_float)
print(type(my_float))
```

Above code gives following output:

```python
>> 43.99
>> <class 'float'>
```


### Arithmetic operations

#### Addition

In Python code, addition can be achieved by writing `number + number`. 

For example, type these operations into the interpreter:
```python
print(20 + 20)
print(21 + 19)
print(5 + 35)
```

All three lines should display the number 40 on your console.

When adding, we can use number variables:
```python
first_number = 18
second_number = 22
print(first_number + second_number)
```

#### Strings addition

It is possible to add strings, not in a mathematical sense, but instead we can join together (concatenate) them:
```python
name = "John"
surname = "Cleese"
print(name + " " + surname)
```

The result will be:
```python
>> John Cleese
```

#### Operations and type conversion

If we try to add a string and an integer, we will get an error:
```python
>>>  "1" + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

```

To fix it (i.e. add 1 and 1 to produce 2), we have to convert the string into integer:
```python
>>> int("1") + 1
2
```

It is important to be aware of types that are used for a given operation. Otherwise, if we have a string, but we try to perform a mathematical operation, we can get a misleading result:
```python
>>> x = "1"
>>> y = "1"
>>> print(x + y)
11
```

To fix this, we have to convert our variables from strings to integers:
```python
>>> int(x) + int(y)
2
```

#### Subtraction

To perform subtraction we use the minus operator:
```python
print(60-20)
```

We can also use variables:
```python
bigger_number = 62
smaller_number = 22
print(bigger_number - smaller_number)
```

#### Multiplication

As in many other languages, the multiplication operator is an asterisk (`*`):
```python
print(3 * 3)
```


#### Powers

Rising to power is done with `**`:
```python
print(3 ** 3)
```

#### Division

The next basic operation is division. 

There are however two versions: it can return a value and a remainder with `/`, or without reminder (with `//`):
```python
print(28 / 3)
print(28 // 3)
>> 9.333333333333334
>> 9
```

#### Remainder

To get just a reminder of the division we use `%`
```python
print(28 % 3)
>> 1
```

The remainder for such a division is 1 because 28 is 3 times 9 plus 1 as a remainder.


#### Order of operations
The order in which operations are performed in Python:

* Operations in brackets
* Multiplication and square rooting
* Multiplication and division (in order of appearance, i.e. from left to right)
* Addition and subtraction (in order of appearance, i.e. from left to right)


## 1.4 Loops
Python has two basic loops:
- for loop
- while loop

### For loop

The `for` keyword is used to create a loop in Python:

```python
for i in range(100):
    print("Hello")
```

A loop exists if and only if we have some repetition. In the example above, the loop will execute 100 times because that's how much we've written into the `range()` function.

We can also print an index of each iteration of the loop:
```python
for i in range(10):
    print(i)
```

This will result in:
```python
0
1
2
3
4
5
6
7
8
9
```

To sum up: A loop consists of a `for` keyword, a variable (in this case `i`), an `in` word, a `range`/`collection` and a loop body/block.
```python
for i in range(1, 11):  # keyword, variable and range
    print(i)  # loop block

```

The variable we've named `i` here can actually be named anything (subject to the variable naming rules, of course). When we do iterations on a numeric collection, you will most often encounter a short, one-character name, often just `i`.

Each time this loop executes, the variable `i` takes on another value from the specified range/collection. So, when the loop executes for the first time, then `i` is equal to 1. On the second execution, `i` has a value of 2, and so on. Successive executions of the loop are called **iterations**.

In the second line we have the body of the loop. As you remember - it must be created with indentation (4 spaces). This block is the commands, the sentences to be executed after each iteration. So in this case, we will be printing the variable `i`, which each time takes the value of the next number in the range.

The loop will terminate when the given range of numbers is exhausted.

### Nested loops

### Loop control

## 1.5 Conditional expressions and booleans

### if-else

### if-elif-else

## 1.6 More loops

### while

### break, continue, pass