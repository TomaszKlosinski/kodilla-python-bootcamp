# Calculator exercise

Let's assume the calculator will always accept only two numbers for calculations.

Ultimately, we would like to achieve this effect:

* When we start the program we are asked for the type of calculation:
```python
>> State the operation, using the appropriate number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division:
```

* We then retrieve two numerical values.

* Using the `logging` library, we tell the user what action we are going to perform and its arguments (e.g. `Adding 1 and 3`).

* We then perform the calculation and print the result with `print()` function.

Use `input()` function to retrieve the values. 

There is no need to check if the given arguments are numbers, we anticipate correct completion.

An example call together with values selected by the user might look like this:

```python
>> Specify the action using the appropriate number: 1 Addition, 2 Subtraction, 3 Multiplication, 4 Division: 1
Enter number 1: 2.3
Enter number 2: 5.4
Adding 2.30 and 5.40
The result is 7.70
```


If you want to improve your solution, you can add two extensions:
* Check that the given value is definitely a number.
* In the case of multiplication and addition, give the user the option to enter more arguments than just two, e.g. you can add three or more numbers together.
