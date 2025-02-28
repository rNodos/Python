# Proyecto final curso Python Essentials 1 Cisco

from random import randint

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.

    separador = "+-------+-------+-------+"
    espacio = "|       |       |       |"

    print(separador)
    for fila in board:
        print(espacio)
        print(f"|   {fila[0]}   |   {fila[1]}   |   {fila[2]}   |")
        print(espacio)
        print(separador)

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

    while True:
        n = int(input("Introduce un número entre el 1 y el 10 que esté disponible en el tablero para asignar tu círculo: "))
        for row in range(3):
            for col in range(3):
                if board[row][col] == n:  # Si el número está en el tablero
                    board[row][col] = "O"  # Reemplaza el número con "X"
                    return  # Sale de la función


def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    
    while True:
        mn = randint(1, 9)  # Genera un número entre 1 y 9
        print(mn)
        for row in range(3):
            for col in range(3):
                if board[row][col] == mn:  # Si el número está en el tablero
                    board[row][col] = "X"  # Reemplaza el número con "X"
                    return  # Sale de la función

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

    # Verifica filas
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return f"¡{sign} gana!"

    # Verifica columnas
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return f"¡{sign} gana!"

    # Verifica diagonales
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return f"¡{sign} gana!"
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return f"¡{sign} gana!"

    return None # Si nadie ha ganado

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.

    print("Turno de la máquina: ")
               
    if board[1][1] == "X":
        make_list_of_free_fields(board)

    while board[1][1] != "X":
        board[1][1] = "X"


    

while True:

    display_board(board)
    draw_move(board)  # Jugador X
    if victory_for(board, "X"):
        display_board(board)
        print("¡Jugador X gana!")
        break

    display_board(board)
    enter_move(board)  # Jugador O
    if victory_for(board, "O"):
        display_board(board)
        print("¡Jugador O gana!")
        break

    # Verificación de empate
    if all(isinstance(cell, str) for row in board for cell in row):
        display_board(board)
        print("¡Empate!")
        break
