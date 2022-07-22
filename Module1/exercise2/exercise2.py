sery = {
    "roquefort": { "cena": 12.50, "waga": 2 },
    "stilton": { "cena": 11.24, "waga": 1 },
    "brie": { "cena": 9.30, "waga": 1 },
    "gouda": { "cena": 8.55, "waga": 1 },
    "edam": { "cena": 11, "waga": 1 },
    "parmezan": { "cena": 16.50, "waga": 3.5 },
    "mozzarella": { "cena": 14, "waga": 1.3 },
    "czechosłowacki ser z owczego mleka": { "cena": 122.32, "waga": 1 }
}

print("Raport z zakupów:\n")
print("Produkt - masa w kg - cena za kg - do zapłacenia")
print("-------------------------------------------------")
suma = 0
for ser in sery:
    do_zaplacenia = sery[ser]['waga'] * sery[ser]['cena']
    print(f"{ser} - {sery[ser]['waga']} kg - {sery[ser]['cena']} zł/kg - {do_zaplacenia} zł")
    suma = suma + do_zaplacenia

print("")
print(f"Suma: {suma:.2f} zł")


