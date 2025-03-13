# Crea una función es_primo(n) que determine si un número es primo.

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    n = int(input("Inserte un número: "))
    
    if n < 0:
        print("Tiene que ser un número positivo")
    else:
        print(f"¿Es primo? {es_primo(n)}")

except ValueError:
    print("Tiene que ser un número.")
