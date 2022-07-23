# Bonus exercise 3:

A list containing the best-selling cars of 2018 ranked from best-seller in `'manufacturer - model'` format was assigned to the `models` variable.

The variables `sales2018`, `sales2017` and `sales2016` were assigned the number of units sold of these models in 2018, 2017 and 2016 respectively.

That is - the best-selling car model in 2018 was: Volkswagen Golf (first position on the `models` list). The Golf sold 445,754 units in 2018 (first position on the `sales2018` list). We also know that 483,105 Golf models were sold in 2017 (first position on the `sales2017` list), and that 492,952 Golfs were sold in 2016 (first position on the `sales2016` list).

Some cars were not sold before 2018. In this case, their sales figures are replaced by 'NA'. Replace all 'NA' with 0.

Build a dictionary with the following structure from the resulting data and **assign it to the `cars`** variable:

```python
cars = {"brand1": {"model1":{"sales":{"2016": 123,
                                     "2017": 456,
                                     "2018": 789}},
                  "model2":{"sales":{"2016": 987,
                                     "2017": 654,
                                     "2018": 321}}
        "brand2": ... }
```

That is, using the real data example, it should look like the following:

```python
cars = { "Opel": {"Corsa":{"sales":{"2016": 264844,
                                   "2017": 232738,
                                   "2018": 217036}},
                 "Astra":{"sales":{"2016": 253483,
                                   "2017": 217813,
                                   "2018": 160275}}
        "Dacia": ... }
```

Then try to answer the questions presented below:

1. which car model from the list sold best in 2017? Assign the answer to the variable `answer1`.
2. Which manufacturer from the list sold the most units of cars in 2018? Assign the answer to the variable `answer2`.
3. How many models of cars from the list did not sell in 2016 and went on sale in 2017? Assign the answer to the variable `answer3`.
4. Which of the car models in the list has the fewest sales if we consider the years 2016, 2017 and 2018. Assign the answer to the variable `answer4`.
5. By how much did sales of Ford models increase in 2018 compared to 2017? Assign the answer to the variable `answer5`. Give the answer in percentage format as a string. E.g. '21%'.

NOTE: For the purposes of the task, treat 'VW' and 'Volkswagen' as separate manufacturers.