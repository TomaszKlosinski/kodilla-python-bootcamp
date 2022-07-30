cheeses = {
    "roquefort": { "price": 12.50, "weight": 2 },
    "stilton": { "price": 11.24, "weight": 1 },
    "brie": { "price": 9.30, "weight": 1 },
    "gouda": { "price": 8.55, "weight": 1 },
    "edam": { "price": 11, "weight": 1 },
    "parmezan": { "price": 16.50, "weight": 3.5 },
    "mozzarella": { "price": 14, "weight": 1.3 },
    "Czechoslovakian": { "price": 122.32, "weight": 1 }
}

print("Shopping report:\n")
print("Product - Weight (kg) - Price per kg - Payment")
print("-------------------------------------------------")
total = 0
for cheese in cheeses:
    payment = cheeses[cheese]['weight'] * cheeses[cheese]['price']
    print(f"{cheese} - {cheeses[cheese]['weight']} kg - ${cheeses[cheese]['price']} per kg - ${payment}")
    total = total + payment

print("")
print(f"Total: ${total:.2f}")


