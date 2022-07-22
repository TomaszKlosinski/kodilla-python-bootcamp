sery = {
    "roquefort": "12,50",
    "stilton": "11,24",
    "brie": "9,30",
    "gouda": "8,55",
    "edam": "11",
    "parmezan": "16,50",
    "mozzarella": "14",
    "czechosłowacki ser z owczego mleka": "122,32"
}

for ser, cena in sery.items():
    print(f"Ser {ser} kosztuje {cena} zł")