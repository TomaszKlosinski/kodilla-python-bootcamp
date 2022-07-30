# Version 1:

for i in range(1,101):
    if i % 3 == 0:
        print(i)


# Version 2:

i = 1
while True:
    if i % 3 == 0:
        print(i)
    if i > 100:
        break
    i = i + 1