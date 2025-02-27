# Pide al usuario un número n y calcula la suma de los primeros n números naturales usando un for.

n = int(input("Inserta un número: "))

suma = 0

for i in range(1, n + 1):
    suma += i

print("La suma de los primeros", n, "números es: ", suma)