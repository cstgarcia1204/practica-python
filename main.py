#Curso
"""
Dado un array de numeros y un numero goal, encuentra los dos primeros numeros del array que sumen el numero goal
y devuelve sus indices. Si no existe etal combinacion, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal) #[2,3]
"""

nums = [4, 5, 6, 2]
goal = 8
#mi solucion junto con la de midu porque el usa en los dos for un range y directamente lo retorna en if yo use extends
def find_first_sum(nums, goal):
    suma_index = []
    for i in nums:
        for j in range(i + 1, len(nums)):
            if  nums[i] + nums[j] == goal:
                suma_index.extend([i, j])
                return suma_index
    return None #No se encontro ninguna combinacion



print(type(find_first_sum(nums, goal)))
print(find_first_sum(nums, goal))

#solucion de midu optimizada usando los diccionarios
###diccionarios
#Los diccionarios son colecciones de pares clave-valor.
#Sirven para almacenar datos relacionados
###
#ejemplo tipico de diccionario

persona = {
    "name": "cinthia",
    "age": 32,
    "es_estudiante": True,
    "calificaciones": [7, 8, 9],
    "socials": {
        "twitter": "@cinthia",
        "facebook": "@cinthia",
        "instagram": "@cinthia"
    }
}
#para acceder a los valores\
print(persona)
print(persona["name"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])
print(persona["socials"]["facebook"])

#cambiar valores al acceder
persona["name"] = "karen"
print(persona["name"])
persona["socials"]["twitter"] = "@karen"
persona["socials"]["facebook"] = "@cin"
persona["socials"]["instagram"] = "@kiiky"


#eliminar completamente una propiedad
del persona["age"]
print(persona)
#si se desea no solo eliminarla sino recuperarla entonces se puede usar pop

es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
print(persona)

#sobreescribir un diccionario con otro diccionario
print("\n sobreescribir un diccionario con otro diccionario")
a = {"name": "cinthia", "age": 32}
b = {"name": "karen", "es_estudiante": False}
print(a)
print(b)

print("\n utilizar update para reescribir")
a.update(b)
print(a)
print(b)

print("\n comprobar si existe una propiedad ->> 'nombre' in persona entonces el resultado es un booleano")
print("nombre" in persona) #False
print("name" in persona) #True

#metodos importantes para obterner todas las claves - valores
print(" \n obtener todas las claves")
print(persona.keys())

print("\n obtener todos los valores")
print(persona.values())

print("\n obtener tanto claves como valor")
print(persona.items())
print(type(persona.items()))

#recorrer los valores con un for
print( "\n recorriendo el diccionario con un for de la manera clave-valor")
for key, value in persona.items():
    print(f"clave: {key} y valor: {value}")

#Solucion para optimizar el ejercicio con diccionarios
print("\n Optimizando la solucion del ejercicio con diccionarios")
def find_first_sum_dict(nums, goal):
    seen = {} #declaramos un diccionario para guardar el nuemero y su indice
    for index, value in enumerate(nums): #aqui regresa indice-valor
        #definimos cual es el faltante para el objetivo
        missing = goal - value
        if missing in seen: #la comparacion es preguntar> el faltante esta en los ya vistos? esto returna True o False
            return [seen[missing], index] #si entra en el true, se retorna una lista donde se esta guardando el indice del anterior que contiene el visto, y el indice actual con index
        seen[value] = index # en el caso de que no se encuentre se asigna el valor en vistos como el indice acutal que estamos repasando en el momento, se asigna el numero actual a vistos



    return None #caso que no se encontro
result = find_first_sum_dict(nums, goal)
print(result)
