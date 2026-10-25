print((1 + 2), type(1 + 2))       # + oznacza dodawanie, wynik to 3 typu int
print((1 + 4.5), type(1 + 4.5))     # + oznacza dodawanie, wynik to 5.5 typu float
print((3 / 2), type(3 / 2))       # / oznacza dzielenie zwykłe, wynik to 1.5 typu float
print((4 / 2), type(4 / 2))       # / oznacza dzielenie zwykłe, wynik to 2.0 typu float
print((3 // 2), type(3 // 2))      # // oznacza dzielenie całkowite, wynik to 1 typu int
print((-3 // 2), type(-3 // 2))     # // oznacza dzielenie całkowite z zaokrągleniem w dół, wynik to -2 typu int
print((11 % 2), type(11 % 2))      # % oznacza resztę z dzielenia, wynik to 1 typu int
print((2 ** 10), type(2 ** 10))     # ** oznacza potęgowanie, wynik to 1024 typu int
print(8 ** (1/3), type(8 ** (1/3)))  # ** oznacza potęgowanie, 1/3 to wykładnik, wynik to 2.0 typu float

print(int(3.0))     # int() zamienia liczbę na całkowitą; wynik to 3
print(float(3))     # float() zamienia liczbę na zmiennoprzecinkową; wynik to 3.0
print(float("3"))   # float() zamienia tekst "3" na liczbę zmiennoprzecinkową; wynik to 3.0
print(str(12.4))    # str() zamienia liczbę na tekst; wynik to "12.4"
print(bool(0))      # bool() zamienia wartość na logiczną; 0 oznacza False (fałsz)