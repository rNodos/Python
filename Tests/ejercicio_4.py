#Pide dos números al usuario y luego intercambia sus valores 
#sin usar una variable auxiliar.

x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))

x, y = y, x

print("Después del intercambio:")
print("Primer número: ", x)
print("Segundo número: ", y)