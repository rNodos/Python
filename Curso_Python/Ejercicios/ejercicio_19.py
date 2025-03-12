# Escribe un programa que pida una oración y muestre:

# La cantidad de palabras
# La cantidad de letras
# La oración en reversa

frase = input("Escribe una frase: ")

palabras = frase.split()
letras = frase.replace(" ", "")
reverso = frase[::-1]

print(f"La cantidad de palabras en la frase es de {len(palabras)} palabras.")
print(f"La cantidad de letras de la frase es de {len(letras)} letras.")
print(f"El texto en reverso es: {reverso}")