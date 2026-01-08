#Curso
# 04 FUNCIONES
# Bloques de codigo reutilizables y parametrizables
"""
Definicion de una funcion
def es de definir la funcion
nombre de la funcion
snakecase
parametros
dos puntos
identacion docstring
retur valor de la funcion es opcional

def nombre_de_la_funcion(parametros):
    #docstring
    #cuerpo de la funcion
    return valor_de_retorno #opcional
"""
#Ejemplo de una funion para imprimir algo en consola
def saludo_mio():
    print("Holi, holi, holi")

saludo_mio() #invocacion de la funcion

#Ejemplo de una funcion con parametro
def saludar_a(nombre):
    print (f"Holi, holi, holi {nombre}!")

saludar_a("Angie")
saludar_a("Astro")

#Funciones con mas parametros
def sumar(a, b):
    return a + b
result = sumar(4, 2)
print(result)

#parametros por defecto
def multiplicar(a, b = 2):
    return a * b
resulto = multiplicar(12)
print(resulto)
#Documentar las funciones utilizando docstring en python, se hace dentro de la funcion
def restar (a, b ):
    """Resta dos numeros y devuelve el resultado"""
    return a -b
#Se puede acceder en el propio lenguaje a la documentacion
print(restar.__doc__)

help(restar)

#Argumentos por posicion y por clave
def describir_persona(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo {edad} anios y me identifico como {sexo}")
#esto significa que los parametros son posicionales
describir_persona("cinthia", 39, "delfin")
#ejemplo cuando los parametros no estan en la posicion que deberia
describir_persona("mujer", "futurista", 38)
#funcion con argumentos por clave, o parametros nombrados
describir_persona (sexo = "delfin", nombre = "cinthia", edad = 39)

#Argumentos de longitud de variable (*args)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(3, 2, 5, 6, 4))
print(sumar_numeros(12, 8, 45))
print(sumar_numeros(3, 2))

#funciones con argumentos de clave-valor variable (**kwargs)
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")
mostrar_informacion_de(nombre="cinthia", edad=39, sexo="mujer")
print("\n")
mostrar_informacion_de(nick="rafael", sexo="hombre", edad=28)
print("\n")
mostrar_informacion_de(edad=27, alias="jesus", sexo="hombre")
print("\n")







