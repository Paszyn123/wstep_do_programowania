def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)

    print("Twoje BMI wynosi:", round(bmi, 2))

    if bmi < 18.5:
        print("Niedowaga")
    elif bmi < 25:
        print("Pożądana masa ciała")
    elif bmi < 30:
        print("Nadwaga")
    elif bmi < 35:
        print("Otyłość I stopnia")
    elif bmi < 40:
        print("Otyłość II stopnia")
    else:
        print("Otyłość III stopnia")

    return bmi


waga = float(input("Podaj swoją wagę w kg: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))

wynik = oblicz_bmi(waga, wzrost)