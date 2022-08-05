dice = {x: set() for x in range(2, 13)}

for i in range(1, 7):
    for j in range(1, 7):
        sum = i + j
        dice[sum].add((i, j))

print(dice)
