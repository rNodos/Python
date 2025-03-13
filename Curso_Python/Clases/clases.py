
class Stack: # Se crea la clase Stack (Pila).
    def __init__(self): # Se inicializa.
        self.__stack_list = [] # Al iniciar crea una lista privada(__) llamada stack_list.

    def push(self, val): # Se crea la función "push"
        self.__stack_list.append(val) # Lo que hace la función es agregar un número al final de la lista.

    def pop(self): # Se crea la función "pop"
        val = self.__stack_list[-1] # Se asigna el último valor de la lista (-1) a la variable (val).
        del self.__stack_list[-1] # Se elimina el último valor de la lista (-1).
        return val # Se muestra/devuelve el valor eliminado.


class AddingStack(Stack): # Se crea una subclase de Stack llamada (AddingStack).
    def __init__(self): # Se inicializa.
        Stack.__init__(self) # Se inicializa la SuperClase para heredar todas las funciones.
        self.__sum = 0 # Se inicializa una variable (sum) en 0.
        
    def get_sum(self): # Definimos la función para devolver el valor de (sum).
        return self.__sum # Devuelve el valor actual de (sum).
        
    def push (self, val): # Definimos otra vez la función "push".
        self.__sum += val # Hacemos que la variable (sum) se sume a la variable (val).
        Stack.push(self, val) # Se llama a la función de la SuperClase "push".
        
    def pop (self): # Definimos otra vez la función "pop".
        val = Stack.pop(self) # Se llama a la función de la SuperClase "pop".
        self.__sum -= val # Hacemos que la variable (sum) se reste a la variable (val).
        return val # Se muestra/devuelve el valor eliminado.
    

stack_object = AddingStack() # Se "invoca" la subclase AddingStack y se crea un objeto (stack_object).

for i in range(5): # Se itera 5 veces.
    stack_object.push(i) # Se ejecuta la función "push" de la subclase que añade la variable "sum" para sumar los números.
print(stack_object.get_sum()) # Se muestra el valor final de la suma de la iteración.

for i in range(5): # Se itera 5 veces.
    print(stack_object.pop()) # Se ejecuta la función "pop" de la subclase que elimina el último valor de la lista y lo muestra por pantalla.

