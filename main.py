#Curso
#03- range()
##Permite crear una secuencia de numeros. Puede ser util para for, pero no solo para eso
###
print("\n Tema range():")
#range no crea un lista es un tipo de dato range
nums = range(5)
#por defecto inicia en 0 el rango, pero se puede personalizar del 2 al 5 --> range(2, 5)
#print(type(nums))
print(nums)
#crea una secuencia de numeros no una lista
for num in range(10):
    print(num)
#permite la secuencia de numeros negativos y paso es decir range(inicio, fin, paso)
for num in range(-4, 3, 2):
    print(num)
#tambien funcionaria con cuentas regresivas, o decremento
for num in range(10, 0, -1):
    print(num)
#Range crea los numeros sobre la marcha es decir es mas rapido porque no almacena en memoria
# permite crear un range de lista
nums = range(10)
list_of_nums = list(nums) #aqui se castea o transforma a lista
print(list_of_nums)

#tambien se puede usar para hacer tareas repetitivas por ejemplo imprimir 4 veces algo
for _ in range(4):
    print("aqui hago una tarea repetitiva")
#la convencion del guion bajo no es propiamente del lenguaje sino es una convencion que si
#si no se va utilizar la variable entonces se pone de esta manera _ y se especifica la tarea que se desea hacer repetidamente

