#Pide al usuario el radio de un círculo y calcula su área usando la fórmula:
#𝐴=𝜋×𝑟2
#Usa math.pi para obtener el valor de π.

import math

rad = int(input("Ingrese el radio del circulo: "))

area = math.pi * rad**2

print("El área del círculo es: ", round(area, 2))