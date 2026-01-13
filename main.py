#Curso
def min_number_of_increments(target_array):
    """
    Calcular el numero minimo de operaciones de incremento de sub-arreglos
    para formar el array objetivo

    Complejidad Temporal: O(n) - una sola pasada.
    Complejidad Temporal: O(1) - sin memoria extra
    """

    total_operations = 0
    previous_value = 0 #Esta es la referencia inicial

    for current_value in target_array:
        # Aqui la logica greedy: Solo acumulamos costo si hay un "Delta Positivo"
        # Es decir, si el valor actual requiere un incremento respecto al anterior.
        if current_value > previous_value:
            # Calculamos la diferencia marginal
            marginal_diference = current_value - previous_value
            total_operations += marginal_diference
        # Actualizamos la referencia para la siguiente iteracion
        # Esto es el valor actual se convierte en el piso del siguiente
        previous_value = current_value
    return total_operations

#target_array = [2, 5, 3, 4]
target_array = [1, 3, 2]
result  = min_number_of_increments(target_array)
print(f"Total de operaciones requeridas: {result}")

"""
Esta es la salida paso a paso la construccion del target
"""
#target = [3, 1, 4, 2]
target = [1, 3, 2]
actual = [0] * len(target)  # Comienza en [0, 0, 0, 0]

# Repetimos mientras no sean iguales
while actual != target:
    # 1. Encontrar el inicio (l) del primer tramo que necesita subir
    l = -1
    for i in range(len(target)):
        if actual[i] < target[i]:
            l = i
            break

    # 2. Encontrar el final (r) del tramo continuo
    # Avanzamos mientras el vecino también necesite subir
    r = l
    while r + 1 < len(target) and actual[r + 1] < target[r + 1]:
        r += 1

    # 3. Sumar 1 a ese rango
    for i in range(l, r + 1):
        actual[i] += 1

    # 4. Imprimir el estado actual
    print(actual)

