zakupy = {
    "Chleb": 5.50,
    "Mleko": 4.00,
    "Masło": 7.50,
    "Ser": 12.00,
    "Jajka": 10.00,
    "Jabłka": 6.00
}

print("Lista zakupów:")

for artykul, kwota in zakupy.items():
    print(artykul, "-", kwota, "zł")

# Podsumowanie wydatków
suma = sum(zakupy.values())

print("Suma wydatków:", suma, "zł")
