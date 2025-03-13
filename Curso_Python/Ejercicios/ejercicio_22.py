# Escribe un programa que:

# Cree un archivo de texto llamado datos.txt
# Pida al usuario su nombre y edad
# Guarde la información en el archivo
# Luego, lea el archivo e imprima los datos en la pantalla

# Paso 1: Pedir datos al usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

# Paso 2: Guardar los datos en un archivo llamado datos.txt
with open("datos.txt", "w") as archivo:
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Edad: {edad}\n")

# Paso 3: Leer el archivo y mostrar su contenido
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()

print("\n📄 Contenido del archivo:")
print(contenido)
