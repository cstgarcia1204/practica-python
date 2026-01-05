#Curso
#02 - Bucles
##Permiten ejecutar un bloque de codigo repetidamente mientras ITERA un iterable o una lista
###
print("\n Bucle for:")
#Iterar una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)
# no solo itera una lista sino cualquier cosa que sea iterable
cadena = "cinthia"
for letra in cadena:
    print(letra)
#Recuperar el indice con for
#enumerate()
print("\n Bucle for con enumerate:")
frutas = ["manzana", "pera", "mandarina"]
for index, fruta in enumerate(frutas):
    print(f"El indice es {index} y la fruta es  {fruta}")
#bucles anidados
letras = ['a', 'b', 'c']
numeros = [1, 2, 3]
for letra in letras:
    for numero in numeros:
        print(f"{letra} x {numero} = {letra*numero}")
#recurso de python tutor para revisar la iteracion paso a paso

#break
print("\n Bucle for con Continue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for index, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro esta escondido en el indice {index}")
        break

print("\n Bucle for con Continue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for index, animal in enumerate(animales):
    if animal == "loro":
        continue
    print(animal)

#comprension de listas/ hacer en una linea el bucle
#lo que hace es que lo puedes devolver y asignarlo a una variable, algo parecido a un map
animales = ["perro", "gato", "raton", "loro", "canario"]
animales_mayusculos = [animal.upper() for animal in animales] #manipular transformando cada elemento y luego usar for en una linea
print(animales_mayusculos)

#Comprension de listas con condicionales if
#Ejercicio tipico muestra los numeros pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)
#esto siempre que se haga la lista manualemte