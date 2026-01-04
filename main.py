#Curso
#Bucles while
#Permiten ejecutar un bloque de codigo conforme se cumpla una condicion
print("\n Bucle while con condicion sin break")
contador0 = 0
contador = 0

#queremos contar del 1 al 5
while contador0 <= 5:
    print(contador0)
    contador0 += 1 # es super importante para evitar un bucle infinitamente

#otra forma de poner una condicion entro de una condicion infinita por el TRUE
print("\n Bucle while sin condicion con break")
while True:
     print("Hola")  #hasta esta linea esto es un bucle infinito
    # break #permite que pare la ejecucion para que no sea infinito
     print(contador + 1)
     contador += 1
     if contador == 5:
         print("Ya me voy, ya cumpli la condicion utilizando el break")
         break #sale del bucle

print("\n While, otro bucle con break pero ahora con condicion")
while contador <= 100:
    print(contador)
    contador += 1
    if contador % 5 == 0:
        print(f"el numero {contador} es multiplo de 5")
        break

#Un bucle con continue
print("\n Bucle while con Continue")
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        print("ya me fui a la siguiente iteracion con continue")
        continue
    print(contador)

#else , esta condicion se ejecuta
print("\n Bucle while con else")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado - cuando la concidicion no se cumple entra aqui tomando en cuenta que no se use con break porque sino da igual no entra aqui")


#Ejercicion con while
print("\n Ejercicio con While")
#pedirle al usuario un numero que tiene
#que ser positivo sino, no le dejamos en paz
numero = -1
while numero < 0:
    try:
        numero = int(input("Introduce un numero: "))
        if numero < 0:
            print("El numero debe ser positivo. Intenta otra vez, mija o mijo. xD")
    except:
        print("Lo que introduces debe ser un numero sino esto no vuela")

print(f"El numero que has introducido es {numero} ")