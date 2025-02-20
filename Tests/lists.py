numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista: ", numbers)

numbers[0] = 111
print("Previo contenido de la lista: ", numbers)

numbers[1] = numbers[4]
print("Nuevo contenido de la lista: ", numbers)

print(numbers[0])

print("Longitud de la lista: ", len(numbers))

print("\n")
del numbers[1]
print("Longitud de la nueva lista:", len(numbers))
print("\nNuevo contenido de la lista:", numbers) 