# Pide al usuario un número e imprime si es positivo, negativo o cero.

n = int(input("Inserta un número: "))

if n < 0:
    print("El número es negativo")

if n > 0:
    print("El número es positivo")

if n == 0:
    print("El número es cero")