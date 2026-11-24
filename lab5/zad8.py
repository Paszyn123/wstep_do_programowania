
# A
def wyswietl(*args):
    for x in args:
        print(x)

wyswietl(1, 5, 10, 2)

# B
def znajdz_max(*args):
    if not args:
        return None
    return max(args)

print(znajdz_max(1, 5, 10, 2))