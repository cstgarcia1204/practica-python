#Curso
"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T'Rex, depositan un número par
de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de
huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribne una función en Python que reciba una lista de números enteros y devielva la suma total de los huevos que
pertenecen a los dinosaurios carnívoros (es decir la suma de todos los números pares en la lista).
"""
"""
Esta es mi solucion propia pero vamos a recrear la del curso midu
"""
def num_huevos(huevos):
    suma = 0
    for huevo in huevos:
        if huevo % 2 == 0:
            suma += huevo
    return suma

print(num_huevos([1, 2, 3, 4, 6, 8, 10])) #30


def count_carnivore_dinosaur_eggs(egg_list) -> int: #Estamos definiendo el tipo de dato que devuelve es un int
    """
    Esta funcion recibe una lista de numeros enteros que representan la cantidad de huevos que han puesto diferentes
    dinosaurios ene l parque jurasico y los de numero par son de carnivoros. Devuelve un numero con la suma
    de todos los huevos de carnivoros.
    """
    total_carnivore_eggs = 0

    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs
    return total_carnivore_eggs
egg_list = [3, 4, 7, 5, 8]
print(count_carnivore_dinosaur_eggs(egg_list))

