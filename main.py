#Curso
### Metodos para las LISTAS
# Los metodos mas importantes para trabajar con listas

#agregar elementos al final de la lista
list1 = [1, 3, 5, 7, 9]
#append solo acepta un parametro
list1.append(11) #agrega un elemento al final
print(list1)

#agregar elemento en una posicion en concreto
#importante recordar que se coloca el indice del cual va tomar posicion porque los elementos los va a empujar hacia adelante para agregarlo
#el indice donde se quiere el elemento se pasa como primer argumento
list1.insert(2, 4) # [1, 3, 4, 5, 7, 9, 11]
print(list1)

# Aniadir elementoSSS al final la diferencia con el append que solo permite uno este metodo permite multiples
#recordar que el conjunto de elementos se debe colocar dentro de una lista de los elementos que se van a agregar
list1.extend([13, 15, 17, 19, 3]) #agrega la lista que determinamos como argumento
print(list1)

#Eliminar elementos de una lista
#Eliminar la primer coincidencia dentro de la lista
#por argumento se pasa el elemento que se quiere eliminar, a diferencia de los anteriores donde se pasa el indice
list1.remove(3) # elimina el primer 3 que encuentra
print(list1)

#metodo pop por defecto elimina el ultimo elemento de la lista y lo devuelve, sin embargo si acepta pasar por argumento los indices
eliminado = list1.pop() # elimina el 3 y lo devuelve es decir lo podemos guardar en una variable
print(list1)
print("Elemento que se aplico el pop ->", eliminado)
# cuando se especifica el indice, incluye indices negativos
list1.pop(2) # Elimina el 4
print(list1)

#otro metodo para eliminar es delete - del y se le pasa el indice, tambien acepta indices negativos
del list1[-3] #elimina el numero 15
print(list1)
# eliminar un rango de elementos con el formato para especificar rangos que son los dos puntos
del list1[3:7] #elimina 9, 11, 13 y 17
print(list1) #queda 1, 4, 7, y 19

#si al final desea eliminar completamente todos los elementos de la lista porque nos hicieron mucho danio xd
list1.clear()
print(list1)

#Metodo para ordenar
print("\n Ordenamiento de listas modificando la original")
list1 = [3, 10, 2, 8, 99, 101]
#Los numeros los ordena de mayor a menor y NO los devuelve es decir no se puede guardar, solo guarda la lista ordenada
list1.sort()
print(list1)

print("\n Ordenamiento de listas creando una nueva lista")
numbers = [3,10,2,8,99,101]
#aqui copia la lista donde tiene los elementos ordenados
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

print("\n Ordenar una lista de cadenas de texto (todo minuscula) ")
frutas = ['manzana', 'pera', 'limon', 'manzana', 'pera']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("\n Ordenar una lista de cadenas de texto (mezcla de mayuscula y minuscula) ")
frutas = ['manzana', 'pera', 'Limon', 'manzana', 'Pera', 'limon']
frutas.sort(key=str.lower)#pasamos cadena de texto a comparar como punto de referencia lowercase
print(frutas)

#metodos para contar cuantas veces aparece algo
animals = ['cat', 'dog', 'cat', 'dog', 'cat']
print(animals.count('cat')) #3
## se puede decir como en pregunta hay un dog en animals?
print('cat' in animals) #devuelve True
print('fog' in animals) # devuelve False