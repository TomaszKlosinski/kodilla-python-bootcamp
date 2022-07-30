# Task 1

print("Cubic roots non-dividable by 2:")
cubic_roots = [x**3 for x in range(1,10)]

for num in cubic_roots:
    if num % 2 != 0:
        print(num)

print("\n")

# Task 2

numbers_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]

print("Slices with zeros:")
print(numbers_list[1:4], numbers_list[5:10], numbers_list[-2:])

print("")

print("Slices with non-zeros:")
print(numbers_list[:1], numbers_list[4:5], numbers_list[10:12])