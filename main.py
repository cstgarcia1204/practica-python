#Curso
#04_Variables
#Las variables sirven para guardar datos en memoria
#python es un lenguaje de tipado dinamico y de tipado fuerte
#Asignar una variable
#Solo hjace falta poner esta sintaxis
my_name = "Cithia"
print(my_name)

age = 32
print(age)
#variables se pueden reasignar
age=38
print(age)

#Tipado dinamico: el tipo de dato se determine en tiempo de ejecucion
#que no tiene que declararlo explicitamente
#Tipado fuerte: No realiza conversiones de tipo automatico
# ejemplo print(10 + "2")

#f-string literal de cadena de formato
print(f"Hola {my_name}, tengo {age -1} anios")

#variables que no se recomienda asignacion de variables
name, age, city = "cinthia", 32, "Guadalajara"
print(name, age, city)

#Convenciones de nombres de variables
mi_nombre_de_variable = "ok" #snake_case
print(mi_nombre_de_variable)

#Convencion que se suele utilizar menos No se recomienda
MiNombreDeVariable = "ko" #PascaleCase
minombredevariable = "ko" #no se recomienda

MI_CONSTANTE = 3.14 #Python no tiene constantes se puede simular creando una clase pero como tal la sintaxis no la tiene
#sin embargo la convencion es UPPER CASE
print(MI_CONSTANTE)
#Nombres no validos de palabras resevadas
#no numeros
#123123_variable
#no guinoes
#mi-variable
#no espacios
#mi variable
#no palabras reservadas
#False, None, True, and, as, assert, async...

#Tipos de variables
is_user_logged_in: bool = True
print(is_user_logged_in)
#si se reasigna ese valor is_user_logged_in a un valor por ejemplo de numero
is_user_logged_in = 456
print(is_user_logged_in)
#EXPLICACION TIPOS DE DATOS
#si lo permite por lo que hay que tener mucho cuidado, aunque el editor lo puede restringir por ejemplo con typecheck
#por defecto Python Analysis: Type Check Mode esta desactivado
#Types Anotation - Types Anotacion - es un comentario en donde estamos documentando al codigo que la variable
#es de booleanom, es una anotacion asi que es posible modificarlo dependiendo la restriccion que se tenga por ejemplo se puede cambiar a >
#basic, standard, strict y si seleccionamos por ejemplo el strict nos saltara en letras rojas en el editor como si fuera un error
#cuando se cambia el tipo de dato porque estamos definiendo un booleano y no un tipo de dato numero
#python no hace ese tipo de revision pero el editor si
# a partir de esa configuracion los tipos de datas los hace estaticos y por ejemplo si a name le asignamos un 32 va saltar el error
#pasa de tipado dinamico a estatico
#no tiene tipos pero se puede
#Recuerda entonces que en si Python no tiene tipos pero si que se puede checkear con el ide para que