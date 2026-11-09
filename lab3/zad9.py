#Wczyta imię i wyświetli powitanie
imie = input("Podaj imię: ")
print(f"Witaj {imie}")

#Wczyta wiek i wyświetli informację
wiek = input("Podaj wiek: ")
print(f"Twój wiek to: {wiek}")

#Wczyta imię i nazwisko oraz wyświetli inicjały
imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
print(f"Inicjały: {imie[0].upper()}.{nazwisko[0].upper()}.")

#Wczyta łańcuch i wyświetli go pięć razy
tekst = input("Podaj łańcuch: ")
print((tekst + "\n") * 5)

#Wczyta dwa łańcuchy, a w trzecim zapamięta połączone
tekst1 = input("Podaj pierwszy łańcuch: ")
tekst2 = input("Podaj drugi łańcuch: ")
tekst3 = tekst1 + tekst2
print(tekst3)

#Wczyta dwa łańcuchy, a w trzecim zapamięta pierwszą połowę pierwszego
tekst1 = input("Podaj pierwszy łańcuch: ")
tekst2 = input("Podaj drugi łańcuch: ")
tekst3 = tekst1[:len(tekst1) // 2]
print(tekst3)