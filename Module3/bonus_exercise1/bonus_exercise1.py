numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0

for index, number in enumerate(numbers):
    if number < 6:
        numbers[index] = 10
    else:
        numbers[index] = round(number, -1)

numbers.sort()
del numbers[0], numbers[-1]

print(numbers)

mean_number = sum(numbers) / len(numbers)

print(mean_number)