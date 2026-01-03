#Curso
# INPUT
#pedir al usuario informacion y poder manipular datos
print("Hola como te llamas")
nombre = input()

print(nombre)

print(f"Hola {nombre}, encantado de conocerte")
### otra forma de hacer el input es directamente la pregunta dentro del input

ciudad = input("y en que ciudad vives?\n")
print(f"excelente la ciudad de {ciudad}")

#
age = input("Cuantos anios tienes?\n")
#siempre la informacion dentro de lo que recibimos en el input siempre es string
print(f"Dentro de 20 anios tendras {int(age) + 20}")

#Obtener multiples valores a la vez
print("Obtener multiples valores a la vez")
#para esto se utiliza la notacion de comas y en el input usamos un split para separa cada valor de cada variable
#por defecto el split por espacio separa todos los elementos de la lista en este caso de input
country, continent = input("en que pais y continente vives?").split()
print(f"Vives en {country} y tu continente es {continent}")