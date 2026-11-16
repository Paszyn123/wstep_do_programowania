Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]


print(Moja_lista)

# 1. Dodawanie elementów



Moja_lista.append(6)
print("append(6):", Moja_lista)

Moja_lista.insert(2, 10)
print("insert(2, 10):", Moja_lista)

Moja_lista.extend([7, 8, 9])
print("extend([7, 8, 9]):", Moja_lista)


# 2. Usuwanie elementów



Lista = Moja_lista.copy()

Lista.remove(3)
print("remove(3):", Lista)

Lista = Moja_lista.copy()
Lista.pop()
print("pop():", Lista)

Lista = Moja_lista.copy()
Lista.clear()
print("clear():", Lista)


# 3. Indeksowanie i wycinanie



print("Lista[0]:", Moja_lista[0])
print("Lista[-1]:", Moja_lista[-1])
print("Lista[1:5]:", Moja_lista[1:5])
print("Lista[1:8:2]:", Moja_lista[1:8:2])


# 4. Sortowanie i odwracanie



print("sort():", sorted(Moja_lista))

Lista = Moja_lista.copy()
Lista.sort()
print("Lista.sort():", Lista)

Lista = Moja_lista.copy()
Lista.reverse()
print("Lista.reverse():", Lista)


# 5. Pozostałe operacje na listach



Lista = [1, 2, 3, 4]

print("Lista:", Lista)
print("len(Lista):", len(Lista))
print("max(Lista):", max(Lista))
print("min(Lista):", min(Lista))
print("sum(Lista):", sum(Lista))


# 6. Łączenie list



lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

Lista = lista1 + lista2
print("lista1 + lista2:", Lista)


# 7. Powielanie listy



ListaM = lista1 * 5
print("lista1 * 5:", ListaM)


# 8. Wyszukiwanie elementu



print("Moja_lista.index(86):", Moja_lista.index(86))


# 9. Dodatkowe wycinanie listy



print("Moja_lista[:]:", Moja_lista[:])
print("Moja_lista[2:6]:", Moja_lista[2:6])
print("Moja_lista[1:9:2]:", Moja_lista[1:9:2])
print("Moja_lista[::-1]:", Moja_lista[::-1])



