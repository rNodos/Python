# Escribe un programa que solicite al usuario dos números y muestre: La suma, La resta, El producto, El cociente (asegurando que no haya división por cero)

n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

print(f"La suma de {n1} y {n2} es igual a: {n1 + n2}")
print(f"La resta de {n1} y {n2} es igual a: {n1 - n2}")
print(f"La multiplicación de {n1} por {n2} es igual a: {n1 * n2}")

if n2 == 0:
    print("No se puede dividir por 0")
else:
    print(f"La división de {n1} entre {n2} es igual a: {n1 / n2}")



