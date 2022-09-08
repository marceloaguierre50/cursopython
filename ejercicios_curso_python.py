# TODO: Crear un diccionario donde el key:value corresponda a la palabra y su correspondiente número

# numeros = [1, 2, 3, 4, 5]
# numeros_Letras = [
#     "uno",
#     "dos",
#     "tre",
#     "cuatro",
#     "cinco"
# ]
# num = {}

# for i in range(len(numeros)):
#     num[numeros[i]] = numeros_Letras[i]

# print(numeros)
# print(numeros_Letras)
# print(num)
# OTRA MANERA DE HACERLO
# num = dict(zip(numeros, numeros_Letras))
# print(num)
# print(type(num))

from os import listxattr
from symtable import Function


palabras = ["python", "rpa", "calyx", "curso", "jupyter", "windows", "lionel hutz"]
# TODO: Crear un diccionario donde el key:value corresponda a la palabra y
# el value sea el texto "La palabra PALABRA posee: X letras"
# Ejemplo: {"python": "La palabra python posee: 6 letras"}
# HACERLO EN CÓDIGO NO MANUALMENTE

"""EL METODO REPLACE ELIMINA LOS ESPACIOS"""
# dic = {}
# for palabra in palabras:
#     palabra = palabra.replace(" ", "")
#     # print(palabra)
#     dic[palabra]= len(palabra)
# print(dic)
"""buscar metodos para eliminar espacios"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# TODO: Iterar la lista y obtener una tupla que contenga los elementos cada 2 saltos
# Hacerlo desde el íncide 0 y el índice 1
# Ejemplo: la tupla quedaría (1, 3, 5, 7, 9)

# lista = []
# for num in range(1, len(numeros),2):
#     lista.append(num)
# print(lista)

diccionario = {
    "acciones": {
        "longitud": len,
        "list": list,
        "set": set,
        "tuple": tuple,
    },
    "datos": {
        "longitud": "Probando diccionarios",
        "list": {1, 2, 3, 4, 5},
        "set": [1, 2, 3, 4, 5],
        "tuple": [1, 2, 3, 4, 5]
    }
}

# TODO: Ejecutar cada acción con su correspondiente dato y agregarlo a una lista vacía
# Ejemplo: acciones->mostrar debería ejecutar datos->mostrar. Esto imprimirá en pantalla "Probando diccionarios" y 
# lo agregará a una lista
# HACERLO EN CÓDIGO NO MANUALMENTE

# lista = [func(diccionario["datos"][value])for value, func in diccionario["acciones"].items()]
lista = []
for value, func in diccionario["acciones"].items():
    lista.append(func(diccionario["datos"][value]))
print(lista)
