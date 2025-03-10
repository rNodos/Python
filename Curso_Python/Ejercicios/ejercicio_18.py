# Crea una lista de números y usa un bucle para calcular la suma y el promedio de los valores.

numeros = [7, 1, 8, 2, 3, 5, 9, 6, 4]

suma = 0

for n in numeros:
    suma += n

promedio = suma / len(numeros)

print("La suma es: ", suma)
print("El promedio es: ", promedio)