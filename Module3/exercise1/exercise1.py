shopping_list = {
    "bakery": ["bread", "doughnut", "bread rolls"],
    "groceries": ["carrots", "celery", "rukola"],
}

print("Shopping list")

total_number_of_items = 0
for shop, items in shopping_list.items():
    capitalized_items = [x.capitalize() for x in items]
    print(
        f"I go to the {shop.capitalize() } and I buy the following items here: {capitalized_items}."
    )

    total_number_of_items = total_number_of_items + len(items)

print(f"In total, I buy {total_number_of_items} products.")
