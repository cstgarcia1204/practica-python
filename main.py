#Curso
#python es importante importa modulos para poder crear herramientas ejemplo
# import os
#os.system("clear")
from win32comext.mapi.mapitags import PR_TYPE_OF_MTS_USER

print("\nSentencia simple condicional")
#sentencia conficional (if, elif, else)
edad = 18
if edad >= 18:
    print("Eres mayor de edad")

#La sintaxis de python es minimalista entonces solo identacion son los bloques
#la ligadura es la fuente de dos caracteres y lo convierten en un simbolo algunos editores se pueden activar
print("\nSentencia condicional con else")
age = 15

if age >= 18:
    print("Eres menor de edad")
else:
    print("Eres menor de edad")
# en python no hay switch case, el else no es obligatorio, es por si se quiere tener una condicion general
print("\nSentencia condicional con elif")
nota = 5
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("No esta calificado")

print("\n Condiciones multiples")
anios = 25
tiene_carnet = False

#python es muy verboso
if anios >= 18 and tiene_carnet:
    print("Puedes conducir ")
else:
    print("Policia ")

if anios >= 18 or tiene_carnet:
    print("Puedes condicir en la isla santa cruz")
else:
    print("Paga policia y te deja conducir ")

#se peude guardar la condicion en una variable
es_fin_de_semana = False
#negar condicion en js es !
if not es_fin_de_semana:
    print("Venga pues vamos al trabajo")

print("\n Anidar condiciones")
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la disco")

#otra forma de resolverlo es cambiar la logica y ahora ir a revisar si es menor de 18 y se simplifica porque se evita la anidacion
if edad < 18:
    print("No puedes entrar a la disco")
elif tiene_dinero:
    print("Puedes entrar a la disco")
else:
    print("Quedate en casa")

#Tipos de datos evaluados como Booleanos
print("\n Tipos de datos evaluados como Booleanos")
#aqui entra el cast es decir la conversion de datos dentro del if
numero = 5
#aqui sabemos que si se evalua como una condicion booleana cuando existe un valor es true
#no hace falta desglosar mas comparacion simplemente una comparacion booleana
if numero: #True
    print("El numero no es cero")

numero = 0
#En este caso que es cero se evalua como false y entonces nunca entra en la condicion en la parte del if
if numero: #False
    print("Aqui no entrar nunca")

#Tambien aplica con las cadenas de texto
#Se evalua de forma logica si la cadena esta vacia
nombre = "Jesus"
if nombre: #True
    print("El nombre no esta vacio")
nombre = ""
if nombre: #False
    print("El nombre esta vacio y nunca entra aqui porque se evalua sobre True")
#Diferncia de comparacion y asignacion importante no olvidar
print("\n Condicion vs Asignacion")
edad = 20
numero = 3 #asignacion
es_el_tres = numero == 3 #comparacion
if es_el_tres:
    print("El numero es 3")

print("\n La Condicion Ternaria")
#una forma concisa de un if else en una linea de codigo
edad = 15
#[codigo si cumple la condicion] if [condicion] else [codigo sino cumple]
print("Es mayor de edad")  if edad >= 18 else print("Es menor de edad")


