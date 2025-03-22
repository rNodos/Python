# Debes poder recordar las reglas que rigen la creación y el uso de un fenómeno de Python llamado listas por comprensión: una forma simple de crear listas y sus contenidos.

# Forma rutinaria
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

# Lista por comprensión
list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)