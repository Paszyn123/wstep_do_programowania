stopnie = (
    "Szeregowy",
    "Kapral",
    "Sierżancie",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik",
)

# 1. Wyznaczenie liczby wszystkich stopni
ilość_stopnii = len(stopnie)

# 2. Znalezienie indeksu elementu "Major"
Major_index = stopnie.index("Major")

# 3. Sprawdzenie, czy "Pułkownik" znajduje się w krotce
Pułkownik_wstepowanie = "Pułkownik" in stopnie

# Wyświetlenie wyników w podanej kolejności
print(ilość_stopnii)
print(Major_index)
print(Pułkownik_wstepowanie)
