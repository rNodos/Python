# Solicita al usuario una palabra y verifica si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda). 

palabra = input("Escribe una palabra: ").lower()  # Convertimos a minúsculas para evitar problemas de mayúsculas
reverso = palabra[::-1]  # Invertimos la palabra

if palabra == reverso:
    print("La palabra es un palíndromo.")
else:
    print("La palabra NO es un palíndromo.")
