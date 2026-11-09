paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo > 0:
    print("Pozostałe paliwo:", paliwo, "litrów")
    paliwo = paliwo - paliwo_zuzyte_na_s
    czas = czas + 1

print(f"koniec lotu czas wynosił: {czas}")