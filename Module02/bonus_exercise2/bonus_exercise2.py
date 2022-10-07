names = [
    "Paweł",
    "Kewin",
    "Ireneusz",
    "Bolesław",
    "Mateusz",
    "Edward",
    "Piotr",
    "Jan",
    "Denis",
    "Amir",
    "Igor",
    "Borys",
    "Robert",
    "Ariel",
    "Kuba",
    "Rafał",
    "Mateusz",
    "Emanuel",
    "Alfred",
    "Artur",
    "Jakub",
    "Ludwik",
    "Bolesław",
    "Remigiusz",
    "Martin",
    "Dobromił",
    "Mariusz",
    "Amadeusz",
    "Łukasz",
    "Bolesław",
    "Amir",
    "Artur",
    "Albert",
    "Olgierd",
    "Alek",
    "Kordian",
    "Julian",
    "Anastazy",
    "Emanuel",
    "Józef",
]

name_dict = {}

for name in names:
    first_letter = name[0]
    name_dict[first_letter] = []

for name in names:
    first_letter = name[0]
    name_dict[first_letter].append(name)

print(name_dict["P"])
