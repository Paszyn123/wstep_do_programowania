import math

def pole_trojkata(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "Z tych boków nie można zbudować trójkąta"
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

try:
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))
    print(pole_trojkata(a, b, c))
except ValueError:
    print("Błędne dane. Podaj liczby.")