x= int(input("Podaj x "))
y= int(input("Podaj y "))
z= int(input("Podaj z "))

if x > y:
    x, y = y, x

if x > z:
    x, z = z, x

if y > z:
    y, z = z, y

print(f"Liczby od najmniejszej do najwiekszej {x}, {y}, {z}")