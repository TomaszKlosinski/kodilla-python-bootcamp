dice = {x: [] for x in range(2,13)}

for i in range(1,7):
    for j in range(1,7):
        sum = i + j
        dice[sum].append((i, j))

print(dice)


