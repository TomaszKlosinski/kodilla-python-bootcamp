"""Exercise 2:
Write a program that:

* For numbers between 0 and 100, display those numbers that are divisible by 5.
* In the next line, it will display those numbers raised to the power of 3.
"""

for n in range(1, 100):
    if n % 5 == 0:
        print(f"{n} -> {n**3}")