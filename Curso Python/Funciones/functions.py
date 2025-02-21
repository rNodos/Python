# Funciones para reutilizar

# Par o Impar
def par_o_impar(n):
    return "Par" if n % 2 == 0 else "Impar"

def es_par_o_impar(n):
    return n % 2 == 0  # True si es par, False si es impar

# Año bisiesto
def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Número Primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Máximo común divisor (MCD)
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Mínimo común múltiplo (MCM)
def mcm(a, b):
    return abs(a * b) // mcd(a, b)

