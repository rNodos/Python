def fib(n):
    if n < 1:  
        return None  # No hay Fibonacci para números menores a 1
    if n < 3:  
        return 1  # Los dos primeros valores de la serie son 1

    elem_1 = elem_2 = 1  # Primeros dos valores de Fibonacci
    the_sum = 0
    
    for i in range(3, n + 1):  # Desde el tercer elemento en adelante
        the_sum = elem_1 + elem_2  # Suma de los dos anteriores
        elem_1, elem_2 = elem_2, the_sum  # Desplazamos los valores
    
    return the_sum  # Retorna el n-ésimo número de Fibonacci
