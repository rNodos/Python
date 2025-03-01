# Pide al usuario una frase y cuenta cuántas palabras tiene.

frase = input("Escribe una frase: ")

palabras = frase.split()

print("La frase tiene", len(palabras), "palabras.")