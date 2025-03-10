#Dada una lista de números, encuentra el número más grande sin usar max().

list = [4, 6, 1, 8, 2, 4, 9, 23, 5, 3, 7]

mayor = list[0]

for i in list:
    if i > mayor:
        mayor = i

print(mayor)