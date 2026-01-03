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



