blocks = int(input("Ingresa el número de bloques: "))

# Inicializar variables
height = 0  # Altura de la pirámide
layer_blocks = 1  # Bloques necesarios para la siguiente capa

# Construcción de la pirámide
while blocks >= layer_blocks:
    blocks -= layer_blocks  # Restar los bloques usados en la capa
    height += 1  # Aumentar la altura de la pirámide
    layer_blocks += 1  # La siguiente capa necesita más bloques

# Dibujar la pirámide
for i in range(1, height + 1):
    print(" " * (height - i) + "#" * (2 * i - 1))  # Pirámide centrada

print("La altura de la pirámide:", height)
