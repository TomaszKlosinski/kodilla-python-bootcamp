# Bonus Exercise 1

## Find the average of the modified list

Your task is to modify the list assigned to the `numbers` variable in such a way that each element of the list is rounded to the nearest ten. Try not to create a new list that is a modified `numbers` list, but modify the `numbers` list instead.

After rounding each element of the `numbers` list, get rid of its largest and smallest element, and then assign the average of the final modified list to the `mean_number` variable.

**Summary:**.

1. round each element of the numbers to the full 10 (e.g. 5 -> 10, 32 -> 30)
2. find and then discard the largest and smallest element of the modified list
3. count the average of the final modified list of `numbers` and assign it to the `mean_number` variable