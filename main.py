#Curso
"""
Esta en Equilibrio la Alianza entre Reed Richards y Jhonny Storm?
En el universo de los 4 Fantasticos, la union y el equilibrio entre los poderes es fundamental para enfrentar
cualquier desafio. Rn este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Jhonny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:
Crea una funcion en Python que reciba una cadena de texto.
Esta funcion debe contar cuantas veces aparece la letra R (para Reed Richards) y
cuantas veces aparece la letra J (para Johnny Storm) en la cadena.

 - Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza
 entre la mente y el fuego esta en equilibrio y la funcion debe retornar True

 - Si las cantidades no son iguales, la funcion debe retornar False.

 - En el caso de que no aparezca ninguna de las dos letras en la cadena,
 se entiende que el equilibrio se mantiene (0=0), por lo que la funcion debe retornar True.
"""
# usar diccionarios
def check_is_balanced(text):
    #transformarlo todo el texto en mayusculas
    text = text.upper()
    #contar facilmente el numero de veces que aparece una letra
    count_r = text.count("R")  #Reed Richards
    count_j = text.count("J")  #Johnny Storm

    print(f"count_r: {count_r} count_j: {count_j}")
    # if count_r == count_j:
    #     return True
    # else:
    #     return False
    #esa condicion con if se puede mejorar porque es muy verbosa entonces directamente retorna la comparacion como se muestra a continuacion:
    return count_r == count_j





print(check_is_balanced("cinthia"))

