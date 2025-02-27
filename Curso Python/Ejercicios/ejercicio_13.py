# El programa genera un número aleatorio entre 1 y 10, y el usuario debe adivinarlo. El programa da pistas de si el número es más alto o más bajo hasta que lo acierte.
import random

rand = random.randint(1, 10)

while n != rand:
    n = int(input("Adivina el número (1 - 10): "))
    if n < rand:
        print("Más")
    elif n > rand:
        print("Menos")
    elif n == rand:
        print("Ese es!")
