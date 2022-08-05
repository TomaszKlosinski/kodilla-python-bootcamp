models = [
    "Volkswagen - Golf",
    "Renault - Clio",
    "Volkswagen - Polo",
    "Ford - Fiesta",
    "Nissan - Qashqai",
    "Peugeot - 208",
    "VW - Tiguan",
    "Skoda - Octavia",
    "Toyota - Yaris",
    "Opel - Corsa",
    "Dacia - Sandero",
    "Renault - Captur",
    "Citroen - C3",
    "Peugeot - 3008",
    "Ford - Focus",
    "Fiat - 500",
    "Dacia - Duster",
    "Peugeot - 2008",
    "Skoda - Fabia",
    "Fiat - Panda",
    "Opel - Astra",
    "VW - Passat",
    "Mercedes-Benz - A-Class",
    "Peugeot - 308",
    "Ford - Kuga",
]

sales2018 = [
    "445,754",
    "336,268",
    "299,920",
    "270,738",
    "233,026",
    "230,049",
    "224,788",
    "223,352",
    "217,642",
    "217,036",
    "216,306",
    "214,720",
    "210,082",
    "204,197",
    "196,583",
    "191,205",
    "182,100",
    "180,204",
    "172,511",
    "168,697",
    "160,275",
    "157,986",
    "156,020",
    "155,925",
    "154,125",
]

sales2017 = [
    "483,105",
    "327,395",
    "272,061",
    "254,539",
    "247,939",
    "244,615",
    "234,916",
    "230,116",
    "199,182",
    "232,738",
    "196,067",
    "212,768",
    "207,299",
    "166,784",
    "214,661",
    "189,928",
    "NA",
    "180,868",
    "180,136",
    "187,322",
    "217,813",
    "184,123",
    "NA",
    "NA",
    "NA",
]

sales2016 = [
    "492,952",
    "315,115",
    "308,561",
    "300,528",
    "234,340",
    "249,047",
    "180,198",
    "230,255",
    "193,969",
    "264,844",
    "170,300",
    "217,105",
    "134,560",
    "NA",
    "214,435",
    "183,730",
    "NA",
    "NA",
    "177,301",
    "191,617",
    "253,483",
    "208,575",
    "NA",
    "195,653",
    "NA",
]

cars = {}


for index, car in enumerate(models):
    brand, model = car.split(" - ")

    cars.update({brand: {}})

for index, car in enumerate(models):
    brand, model = car.split(" - ")

    cars[brand] = cars[brand] | {model: {}}

for index, car in enumerate(models):
    brand, model = car.split(" - ")

    cars[brand][model] = {
        "sales": {
            "2016": sales2016[index].replace(",", ""),
            "2017": sales2017[index].replace(",", ""),
            "2018": sales2018[index].replace(",", ""),
        }
    }

print("Cars Dictionary:")
print(cars)
print("")


# Question 1: Which car model on the list had best sales in 2017?

top_model_2017 = {"car": "", "sales": 0}
for brand in cars.keys():
    for model in cars[brand].keys():
        model_sales2017 = cars[brand][model]["sales"]["2017"]
        if model_sales2017 != "NA":
            if top_model_2017["sales"] < int(model_sales2017):
                top_model_2017 = {
                    "car": f"{brand} {model}",
                    "sales": int(model_sales2017),
                }

answer1 = top_model_2017
print(f"answer1: {answer1}")


# Question 2: Which manufacturer on the list sold the most cars in 2018?

manufacturers_total_sales_2018 = {car.split(" - ")[0]: 0 for car in models}
for brand in cars.keys():
    for model in cars[brand].keys():
        model_sales2018 = cars[brand][model]["sales"]["2018"]
        if model_sales2018 != "NA":
            manufacturers_total_sales_2018[brand] = manufacturers_total_sales_2018[
                brand
            ] + int(model_sales2018)

top_manufacturer_2018 = max(
    manufacturers_total_sales_2018, key=manufacturers_total_sales_2018.get
)

answer2 = f"{top_manufacturer_2018} - total sales: {manufacturers_total_sales_2018[top_manufacturer_2018]}"
print(f"answer2: {answer2}")


# Question 3: How many models of cars on the list did not sell in 2016 and went on sale in 2017?

car_models_on_sale_2017 = []
for brand in cars.keys():
    for model in cars[brand].keys():
        model_sales2016 = cars[brand][model]["sales"]["2016"]
        model_sales2017 = cars[brand][model]["sales"]["2017"]
        if model_sales2016 == "NA" and model_sales2017 != "NA":
            car_models_on_sale_2017.append(f"{brand} - {model}")

answer3 = car_models_on_sale_2017
print(f"answer3: {answer3}")


# Question 4: Which of the car models in the list has the fewest sales if we consider 2016, 2017 and 2018.

car_sales2016 = 0
car_sales2017 = 0
car_sales2018 = 0

cars_total_sales = {car: 0 for car in models}
for brand in cars.keys():
    for model in cars[brand].keys():
        car = f"{brand} - {model}"
        if cars[brand][model]["sales"]["2016"] != "NA":
            car_sales2016 = int(cars[brand][model]["sales"]["2016"])
        if cars[brand][model]["sales"]["2017"] != "NA":
            car_sales2017 = int(cars[brand][model]["sales"]["2017"])
        if cars[brand][model]["sales"]["2018"] != "NA":
            car_sales2018 = int(cars[brand][model]["sales"]["2018"])

        total_sales = car_sales2016 + car_sales2017 + car_sales2018
        cars_total_sales[car] = total_sales

car_least_total_sales = min(cars_total_sales, key=cars_total_sales.get)

answer4 = (
    f"{car_least_total_sales} - total sales: {cars_total_sales[car_least_total_sales]}"
)
print(f"answer4: {answer4}")


# Question 5: By how much did sales of Ford models increase in 2018 compared to 2017 (in percentage)?

ford_cars_sales_2017 = 0
ford_cars_sales_2018 = 0
for brand in cars.keys():
    if brand == "Ford":
        for model in cars[brand].keys():
            model_sales2017 = cars[brand][model]["sales"]["2017"]
            model_sales2018 = cars[brand][model]["sales"]["2018"]
            if model_sales2017 != "NA":
                ford_cars_sales_2017 += int(model_sales2017)
            if model_sales2018 != "NA":
                ford_cars_sales_2018 += int(model_sales2018)

sales_increase_2018 = ford_cars_sales_2018 / ford_cars_sales_2017 - 1
answer5 = "{0:.0%}".format(sales_increase_2018)
print(f"answer5: {answer5}")
