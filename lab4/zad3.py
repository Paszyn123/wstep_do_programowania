
# a. Wczytanie imienia i wyświetlenie powitania

imie = input("Podaj imię: ")
print("Witaj", imie)


# b. Wczytanie wieku i wyświetlenie go

wiek = input("Podaj swój wiek: ")
print("Twój wiek to:", wiek)


# c. Wczytanie imienia i nazwiska oraz wyświetlenie inicjałów

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

inicjaly = imie[0] + "." + nazwisko[0] + "."
print("Twoje inicjały:", inicjaly)


# d. Wczytanie łańcucha i wyświetlenie go pięć razy

tekst = input("Podaj dowolny tekst: ")
print("Tekst pięć razy:", tekst * 5)


# e. Wczytanie dwóch łańcuchów i połączenie ich

tekst1 = input("Podaj pierwszy łańcuch: ")
tekst2 = input("Podaj drugi łańcuch: ")

tekst3 = tekst1 + tekst2
print("Połączone łańcuchy:", tekst3)


# f. Pierwsza połowa pierwszego i druga połowa drugiego łańcucha

tekst1 = input("Podaj pierwszy łańcuch: ")
tekst2 = input("Podaj drugi łańcuch: ")

polowa1 = tekst1[:len(tekst1)//2]
polowa2 = tekst2[len(tekst2)//2:]

tekst3 = polowa1 + polowa2

print("Wynik:", tekst3)
