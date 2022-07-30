cheeses = {
    "roquefort": "12,50",
    "stilton": "11,24",
    "brie": "9,30",
    "gouda": "8,55",
    "edam": "11",
    "parmezan": "16,50",
    "mozzarella": "14",
    "Czechoslovakian": "122,32"
}

for cheese, price in cheeses.items():
    print(f"Cheese {cheese} costs ${price}")