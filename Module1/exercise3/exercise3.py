print("Picture nr 1")
for i in range(10):
    if i % 2 != 0:
        poczatek = ' '
    else:
        poczatek = ''

    print(f'{poczatek}' + '* ' * 10)


print("\n\n")
print("Picture nr 2")
for i in range(2, 8, 2):
    print('* ' * i)
    print('* ' * i)



print("\n\n")
print("Picture nr 3")
for i in reversed(range(7)):
    print('*' * i)