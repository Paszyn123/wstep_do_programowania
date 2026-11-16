
# Utworzenie listy z imionami 4 osób
imiona = ["Anna", "Piotr", "Kasia", "Marek"]

print("Lista początkowa:", imiona)

# a. Sortowanie alfabetyczne
imiona.sort()
print("a. Lista posortowana alfabetycznie:", imiona)

# b. Dodanie dwóch osób na końcu listy
imiona.append("Tomasz")
imiona.append("Zuzanna")
print("b. Po dodaniu dwóch osób:", imiona)

# Pobranie ostatniej osoby za pomocą pop()
ostatnia_osoba = imiona.pop()
print("Pobrana ostatnia osoba:", ostatnia_osoba)
print("Lista po pop():", imiona)

# c. Dodanie osoby na pozycji 3
imiona.insert(2, "Karol")
print("c. Po dodaniu osoby na pozycji 3:", imiona)

# d. Odwrócenie kolejności listy
imiona.reverse()
print("d. Lista po odwróceniu:", imiona)

# Zdublowanie listy
imiona = imiona * 2
print("Lista po zdublowaniu:", imiona)
