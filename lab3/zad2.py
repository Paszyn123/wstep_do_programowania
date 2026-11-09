liczba = 2
licznik = 0
lista_liczb_pierwszych = []

while licznik < 10:
    for i in range(2, liczba):
        if liczba % i == 0:
            break
    else:
        lista_liczb_pierwszych.append(str(liczba))
        licznik += 1
    liczba += 1
print(", ".join(lista_liczb_pierwszych))