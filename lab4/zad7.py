moja_krotka = (10, 2, 6, 6, 9, 13, 0, 1)

print("Krotka początkowa:", moja_krotka)

# Zamiana krotki na listę
moja_lista = list(moja_krotka)

# Sortowanie listy rosnąco
moja_lista.sort()

# Ponowna zamiana listy na krotkę
moja_krotka = tuple(moja_lista)

print("Krotka po sortowaniu:", moja_krotka)
