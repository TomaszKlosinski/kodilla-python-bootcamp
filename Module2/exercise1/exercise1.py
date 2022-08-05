# Task 1

name_list = ["John", "Michael", "Terry", "Eric", "Graham"]

name_dict = {}

for name in name_list:
    name_dict[name] = len(name)

print(name_dict)


# Task 2

numbers = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
prime_numbers = []


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


for number in numbers:
    if is_prime(number):
        prime_numbers.append(number)

print(prime_numbers)


# Task 3

week_days = ["pon", "śro", "pią", "sob"]
week_days.insert(1, "wto")
week_days.insert(4, "czw")
week_days.insert(6, "nie")

print(week_days)


# Task 4

actions_list = [
    "włącz czajnik",
    "znajdź opakowanie herbaty",
    "zalej herbatę",
    "nalej wody do czajnika",
    "wyjmij kubek",
    "włóż herbatę do kubka",
]
orderd_actions_list = []

orderd_actions_list.append(actions_list[3])
orderd_actions_list.append(actions_list[0])
orderd_actions_list.append(actions_list[4])
orderd_actions_list.append(actions_list[1])
orderd_actions_list.append(actions_list[5])
orderd_actions_list.append(actions_list[2])

print(orderd_actions_list)
