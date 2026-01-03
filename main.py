#Curso
### 03 Casting de types
# Transformar un tipo de un valor a otro
###

print("Conversion de tipos")
print("string --> int ")
print(int("100")+1)
print(type(int("100")+2))

print("redondeado")
print(type(float("3.1416")))
print(type(int(3.1416)))
print(int(3.1416))

#booleanos
#El unico que se transforma en False de estos 3 casos es el cero para que se tenga en cuenta
print(bool(3))
print(bool(0))
print(bool(-1))

#para estos casos el espacio ya se considera que tiene algo entonces no es cadena vacia
print(bool(""))
print(bool(" "))
print(bool("False"))
print(bool("True"))
