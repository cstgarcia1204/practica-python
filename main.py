#Curso
"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud.

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b) # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""

#respuesta propia
def battle(lista_a, lista_b):
    """
    recibe dos listas de n batallas
    se comparan los elementos de cada lista mediante la suma de sus elementos
    se crea la condicion si a es mayor que b entonces saca la diferencia de a y retornar ese valor

    debe existir una diferencia definida para saber con cuanto gana con cada lista a o si es b
    sino es ninguno de los dos entonces es igual asi que se manda al else
    :param lista_a:
    :param lista_b:
    :return: un valor que representa por un lado la batalla y por otro lado a que lista pertenece concatenado
    """
    puntos_a = sum(lista_a)
    print(puntos_a)
    puntos_b = sum(lista_b)
    print(puntos_b)


    if puntos_a > puntos_b:
        diferencia = puntos_a - puntos_b
        return f"{diferencia}a"
    elif puntos_b > puntos_a:
        diferencia = puntos_b - puntos_a
        return f"{diferencia}b"
    else:
        return f"x"



   #respuesta de midu super elegante
    #return  f"{puntos_a - puntos_b}a" if puntos_a > puntos_b else f"{puntos_b - puntos_a}b" if puntos_b > puntos_a else "x"


#lista_a = [4, 4, 4]
#lista_b = [2, 8, 2]
lista_a = [2, 4, 1]
lista_b = [3, 3, 4]
print(battle(lista_a, lista_b))

