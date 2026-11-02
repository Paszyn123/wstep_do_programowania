litera = input("Podaj litere: ")

if litera.isalpha() and len(litera)==1:
    if litera.isupper():
        print("litera jest duza")
    elif litera.islower():
        print("litera jest mala")
else:
    print("wprowadzony znak nie jest pojedyncza litera")