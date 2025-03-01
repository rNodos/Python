# Dada una lista de números, crea una nueva lista que contenga solo los números pares.

list = [4, 6, 1, 8, 2, 4, 9, 23, 5, 3, 7]

new_list = []

for num in list:
    if num % 2 == 0:
        new_list.append(num)

print(new_list)