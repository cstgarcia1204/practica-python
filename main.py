#Curso
# 03 Listas
#Secuencias mutables de elementos. Pueden contener elementos de diferentes tipos.
##  Una lista no deja de ser la posibilidad de tener un conjunto de elementos uno detras de otros

#Creacion de listas
print("\n Creacion de listas")
lista1 = [1, 3, 5, 7, 9]
lista2 = ["manzanas", "peras", "platanos"]
lista3 = [1, "hola", 3.14, True] # lista de tipo mixtos, es posible pero se puede indicar tipos o restgtingir lista3: list[int]
lista_vacia = []
lista_de_listas = [[1, 2], [2, 3], [4, 5]]
matrix = [[1,2], [3,4], [5,6]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

#Accedo a elementos por indice
print("\n Acceso a elementos por indice")
print(lista2[0]) #manzanas
print(lista2[1]) #peras
#para la ultima posicion pytrhon permite los indices negativos que irian desde atras hacia adelante
print(lista2[-1]) #platanos
print(lista2[-2]) #peras

#lista de listas
print(lista_de_listas[1][0]) #numero 2 (el primer corchete es el elemnto en este cas0 [1] = [2,3]
## despues el elemnto [0] hace referencia a lo que contiene internamente en este caso el indice 0 es el numero 2 y el indice 1 es el numero 3
print(lista_de_listas[1][1]) #numero 3

#slicing de listas se indica desde el indice hasta el indice que se quiere pero ese ultimo no lo incorpora otra forma de verlo es desde el inicio de cada indice tanto cuando empieza, como cuando finaliza
print(lista1[1:4]) #3, 5, 7
#se peude indicar los 3 primeros numeros
print(lista1[:3]) #1, 3, 5
#se puede los ultimos 3
print(lista1[2:]) #5, 7, 9
#copia de la lista
print(lista1[:]) #1, 3, 5, 7, 9

#paso de listas
#por default el paso es de 1 a 1 pero se puede personalizar
print(lista1[::2]) #1, 5, 9
print(lista1[1::2]) #3, 7
#como acepta indices negativos entonces el paso funciona como revertido
print(lista1[::-1])#9, 7, 5, 3, 1

#Modifica una lista
lista1[0] = 20
print(lista1)
#SI SE INTENTA ACCEDER A UN INDICE QUE NO EXISTE, NO LO VA PERMITIR

# Aniadir elementos a una lista
lista1 = [1, 2, 3]
print(lista1)
lista1 = lista1 + [4, 5, 6]
print(lista1)
#forma mas corta y eficiente porque no guarda en memoria la lista1 + lo que se agregue sino que directamente lo agrega
lista1 += [7, 8, 9]
print(lista1)

#Recuperar longitud de una lista
print("La longitud de la lista es: ", len(lista1))

