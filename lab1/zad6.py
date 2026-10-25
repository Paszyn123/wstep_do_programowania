import random

droga = random.randint(100, 1000)
spalanie = float(input("Podaj srednie spalanie w litrach na 100 km: "))
cena = float(input("Podaj aktualna cene paliwa za litr w zl: "))

zuzycie = droga * spalanie / 100
koszt = zuzycie * cena

print(f"Dlugosc drogi: {droga} km")
print(f"Przewidywane zuzycie paliwa: {zuzycie:.2f} l")
print(f"Szacowany koszt podrozy: {koszt:.2f} zł")