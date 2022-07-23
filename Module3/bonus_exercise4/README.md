# Throwing the dice

We play a game of throwing a typical cubic dice.

Each turn a player throws the dice twice. After the dice have been thrown twice, the player's score is the sum of the dots thrown from throw number 1 and throw number 2.

Write a program that assigns pairs `key` and `value` to the `dict` dictionary, where:

- `key` - is the possible result in one queue (the sum of the meshes in two throws)
- value - is all combinations of throws that make up a given `key`.

Store all possible combinations to get a given result as a set, where each successive element is a `key`, whose first value is the result of the first throw, and whose second value is the result of the second throw.

For example, by calling:

```
dice[7]
```

The result should contain the following elements:

```
{(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)}
```

