# Module 4

## 4.1 Introduction to the functions

### Definition and call

Functions are available in many languages. In Python, we define them as follows:

```python
def demo_function():
    print("I am inside of a function!")
```

Notice that we start with the def command. Then we write the name of the function with parentheses, a colon (:), and then its body on the following lines. The body is a block, which is governed by its own rules (as a reminder - a block is a piece of code where all lines have the same indentation, so remember to format properly with spaces).

That's not all, however. A function is a block of code that only executes when it is called.

How do you do this? By using a name and round brackets.

```python
demo_function()
```

After calling the above function, you will see this result:

```python
>>> I am inside of a function!
```

Great, you have successfully created your first function and named it. And while we're on the subject of "naming". As with variables, in addition to following some pre-imposed general rules, we want to stick to good programming practices. According to these - the name should describe what the function does. Having, for example, print_hello_world(), we can immediately deduce what to expect from it.

There are also other official PEP8 guidelines that are worth reading and following.

