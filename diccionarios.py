"""COMO CREAR  UN DICCIONARIO"""

# familia = {"marcelo" : 33,
#            "lorena": 35,
#            "ian": 8,
#            "zoe": 3,
#            "gema":2}

"""COMO OBTENER LOS VALUES Y KEYS EN UN DICCIONARIO"""

# print(familia.values())
# print(familia.keys())
# print(familia.items())
# print(len(familia))
# print(familia)

# """BORRAR ELEMENTOS DE UNA LISTA mediante sentencia DELL"""
# del(familia["gema"])
# print(familia)
"""Por su clave (con extracción): Mediante la función pop() podemos extraer un elemento
del diccionario por su clave. Vendría a ser una combinación de get() + del:"""
# familia.pop("marcelo")
# print(familia)

"""COMO VACIOIAR UNA LISTA POR COMPLETO"""
# familia.clear()
# print(familia)

"""Cuidado con las copias"""

# copy_famili = familia
# copy_famili = familia.copy()
# del(familia["ian"])
# print(familia)
# print(copy_famili)

"""DICCIONARIO POR  COMPRENCION
Veamos un ejemplo en el que creamos un diccionario por comprensión donde las claves
son palabras y los valores son sus longitudes:"""
familia = ("marcelo", "lorena", "ian", "gema", "zoe")
print(type(familia))
# famila_copy = {word:len(word) for word in familia}

# print(famila_copy)

"""También podemos aplicar condiciones a estas comprensiones. Continuando con el ejemplo
anterior, podemos incorporar la restricción de sólo incluir palabras que no empiecen por
vocal:"""
famili_copi = {w: len(w) for w  in familia if w[0] not in "aeiou"}

print(famili_copi)



"""ITERAR SOBRE CLAVES"""
# for i in familia.values():
#     print(i)

"""PARA VER SI UN ELEMENTO  ESTA DENTRO  DE UNA LISTA"""
# print("marcelo" in familia)

# print(familia)

# print(familia)
# print(type(familia))
# print(familia)

"""OBTANER UN ELEMENTO DEL DICCIONARIO"""

# print(familia["lorena"])
"""USANDO EL GET Existe una función muy útil para «superar» los posibles errores de acceso por claves
inexistentes. Se trata de get() y su comportamiento es el siguiente:
1. Si la clave que buscamos existe, nos devuelve su valor.
2. Si la clave que buscamos no existe, nos devuelve None 4 salvo que le indiquemos otro
valor por defecto, pero en ninguno de los dos casos obtendremos un error."""

# print(familia.get("ale","no disponible"))

"""COMO AGREGAR UN ELEMENTO  A UN DICCIONARIO"""

# familia ["ale"] = 30
# print(familia)

"""Supongamos un ejemplo en el que queremos construir un diccionario donde las claves son
las letras vocales y los valores son sus posiciones:
"""
# vocales = "aeiou"
# # print(vocales)
# enum = {}
# for i, VOCALES in enumerate (vocales):
#     enum[VOCALES] = i + 1
    
# print(enum)

"""Usando un diccionario, cuente el número de veces que se repite cada letra en una cadena de
texto dada.
Ejemplo
• Entrada: boom
• Salida: { b : 1,
o : 2, m : 1}"""
