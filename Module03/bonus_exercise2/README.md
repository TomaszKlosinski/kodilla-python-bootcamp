# Bonus Exercise 2

## Function that checks if we can build a bridge

Our task is to build a bridge between point A and point B.

We are given a **chunk** and a **junction**, both of which have specific lengths.

The chunks cannot be divided into smaller pieces, we place them side by side. The chunks must be connected to each other using a junction. The junction is half the length of the plate.

Create a function `build_bridge()` that will return `True` if, given the length of `chunk`, we are able to build a bridge of length given by the variable `goal`.

Let the function `build_bridge()` return the value `False` if building a bridge given the variables `chunk` and `goal` is not possible.

For example:

* If `goal` is 20 and `chunk` is 2 - then we can use 7 plates and 6 connectors. We can build a bridge, and the function should return the value `True`.
* On the other hand, if `goal` is 18 and `chunk` is 2 - then we can NOT build a bridge, and the function should return the value `False`.
