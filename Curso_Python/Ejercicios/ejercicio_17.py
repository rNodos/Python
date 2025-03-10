# Escribe un programa que almacene una lista con 5 nombres. Luego:

# Pida al usuario un nombre
# Verifique si está en la lista y muestre un mensaje adecuado

nombres = ["Dan", "Pepe", "Jose", "Maria", "Eric"]

user = input("Escribe un nombre: ").strip().capitalize()

if user in nombres:
    print(f"El nombre de {user} está en la lista.")
else:
    print(f"El nombre de {user} no está en la lista.")