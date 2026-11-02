punkty= int(input("Podaj liczbe punktow "))
if punkty >80:
    print("Zaliczyles egzamin w terminie zerowym")
elif punkty >=50 and punkty <=80:
    print("Mozesz poprawic swoj wynik")
elif punkty <50:
    print("Musisz poprawic wynik egzaminu")