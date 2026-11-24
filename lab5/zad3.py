def powitanie(imie="Użytkowniku", jezyk="polski"):
    if jezyk == "polski":
        print("Cześć,", imie)
    elif jezyk == "angielski":
        print("Hello,", imie)
    elif jezyk == "niemiecki":
        print("Guten Morgen,", imie)
    else:
        print("Witaj,", imie)


powitanie()
powitanie("Anna")
powitanie("John", "angielski")
powitanie("Hans", "niemiecki")
powitanie("Adam", "francuski")