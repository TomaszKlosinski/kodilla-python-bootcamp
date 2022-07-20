"""
Szef organizuje przyjęcie dla klientów i wysłał Cię do sklepu z serami. Wiadomo jak to jest z tego typu instytucjami [*], czasami półki świecą pustkami, ale powiedzmy, że po długich poszukiwaniach udało Ci się znaleźć dobrze wyposażony i kupić wszystko, co potrzeba (oprócz mocno przechodzonego camemberta).

Nie bojąc się stringów ani ich formatowania, skorzystaj z dotychczasowej wiedzy i stwórz raport. Zaskocz swojego szefa rzeczową listą zakupów wraz z cenami.

W Twoim koszyku znalazł się kilogram każdego z tych serów: roquefort (12,50 zł), stilton (11,24 zł), brie (9,30 zł), gouda (8,55 zł), edam (11 zł), parmezan (16,50 zł), mozzarella (14 zł) oraz hit – czechosłowacki ser z owczego mleka (122,32 zł).

Stwórz odpowiednie zmienne, zarówno dla produktów, jak i cen. Umieść wszystko w jednym tekście i użyj odpowiedniego formatowania. Pamiętaj, że ceny w Polsce zwykło się podawać z dwoma miejscami dziesiętnymi po przecinku (w Pythonie, zgodnie z anglosaską tradycją, używamy kropki zamiast przecinka, więc w kodzie napiszemy 2.49, a nie 2,49).
"""

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