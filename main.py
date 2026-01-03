#Curso
#Booleanos
#Valores logicos: True (Verdadero) y False(falso)
#Fundamentales para el control de flujo y la logica en programacion
###
print("\n Valores booleanos basicos:")
print(True)
print(False)

#Operadores de comparacion: devuelven un valor boolean
print("\n Operadores de comparacion")

print("5 > 3", 5 > 3) #True
print("5 < 3", 5 < 3) #False
print("5 == 5", 5 == 5) #True (igualdad, no hace falta 3 iguales ni nada con solo dos)
print("5 != 3", 5 != 3) #True (desigualdad)
print("5 >= 5", 5 >= 5) #True (mayor o igual que)
print("5 <= 3", 5 <= 3) #False (menor o igual que)

print("\n Comparaciones de cadenas")
print("'manzana' < 'pera':", "manzana" < "pera") #True - Revisa el orden alfabetico asi que la m si es mas pequenia que la p de pera
print("'Hola' == 'hola'", "Hola" == "hola" ) #False - Sensitive case

##Operadores logicos: and, or, not
print("\n Operadores logicos")
print("True and True", True and True) # True
print("True and False", True and False) #False
print("True or False", True or False) #True
print("False or False", False or False) #False
print("not True", not True) #False
print("not False", not False) #True

print("\n Tablas de Verdad")
print("\n and:")
print("A         B    A  and  B ")
print("True  True      ", True and True)
print("True  False     ", True and False)
print("False  True     ", False and True)
print("False  False    ", False and False)

print("\n or:")
print("A         B    A  or  B ")
print("True  True      ", True or True)
print("True  False     ", True or False)
print("False  True     ", False or True)
print("False  False    ", False or False)

print("\n not:")
print("A       not A")
print("True    ", not True)
print("False    ", not False)
