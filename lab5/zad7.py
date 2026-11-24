def potega(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / potega(a, -n)
    return a * potega(a, n - 1)

a = float(input("Podaj a: "))
n = int(input("Podaj n: "))
print(potega(a, n))