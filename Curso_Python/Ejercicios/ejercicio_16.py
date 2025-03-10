# Crea un programa que simule un cajero automático. El usuario tiene un saldo inicial de $1000 y puede:

# Depositar dinero
# Retirar dinero (validando que tenga saldo suficiente)
# Consultar saldo
# Salir

saldo = 1000

while True:
           
    try: 
        user = int(input("\n¿Que deseas hacer?\n1.Depositar\n2.Retirar dinero\n3.Consultar saldo\n4.Salir\n"))
        
        if user == 1:
            dep = int(input("\n¿Cuánto desear depositar? "))
            if dep > 0:          
                saldo += dep
                print(f"Saldo actual = {saldo}")
            else:
                print("\nEl monto debe ser mayor a 0.")
        
        elif user == 2:
            ret = int(input("\n¿Cuánto desear retirar? "))
            if ret > 0:
                if ret <= saldo:
                    saldo -= ret
                    print(f"\nSaldo actual = {saldo}")
                else:
                    print("No tienes suficiente saldo")
            else:
                print("\nEl monto debe ser mayor a 0.")
        
        elif user == 3:
            print(f"Saldo actual = {saldo}")   
        
        elif user == 4:
            print("\nSaliendo del cajero")
            break
        
        elif user == 0 or user > 5:
            print("\nIngresa una de las opciones en pantalla.")

    except ValueError:
        print("\nError: Ingresa un número válido.")