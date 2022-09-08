"""como crear una lista"""

# lista = ["lunes", "martes","miercoles","jueves","viernes"]

# print(lista)

"""listas anidadas"""

# nombre = ["marcelo", "lucas", "matias", "valeria"]
# edad = [18, 21, 33, 44]

# amigos =[["marcelo",18],
#         ["lucas",21],
#         ["matias",33],
#         ["valeria",44]]

"""como cambiar un dato de una lista"""

# amigos [2][0] = "pepe"
# print((amigos))
# amigos [3][1]=25
# print(amigos)

# print(amigos[3][1])
# print(amigos)

"""agregar un dato a una lista"""

# amigos.append(["zara"])
# amigos[4].append(22)
# print(amigos)

"""otra manera de mostrar la listas y sus datos"""

# for amigo in amigos:
#     print("{:}: {:}".format(amigo[0],amigo[1]))
#     print("{:20}: {:2}".format(amigo[0],amigo[1]))
    
"""en una tienda quieren hacer un inventario de las figuras que tienen y el numero de unidades
de cada una. crea una lista que contengan los datos del inventario:
6 cuadrados, 5 circulos, 4 triangulos y 3 rectangulos"""
# inventario = [["circulo",5],
#               ["cuadrado",6],
#               ["triangulo",4],
#               ["rectangulo",3]]
# print(inventario)

"""me creo una lista llamadas numeros"""

# numeros =[1, 2, 3, 4, 5]
# print(numeros)
# primeraPosicion = numeros [0]
# print(primeraPosicion)
# print(numeros[0])

"""metodo len() me muestra la longitud de una lista"""

# longitud = len(numeros)
# print(longitud)

""" lo que me esta diciendo es que: el primer valor es 1 y su longitud es 5"""
""" la \n se usa para saltar al renglon de abajo"""

# print(f"el primer valos es:{primeraPosicion}\n la losgitud de la lista es:{longitud}")

# for num in numeros:
#     print(num)
# print((numeros))

"""Apartado 2: indexado y  sublistas"""

# lista = ["dale", "un", "buen", "like", "crak"]
# print(lista)

# ultimaPosicion = lista[-1]
# print(ultimaPosicion)

# penultimo = lista[-2]
# print(penultimo)

# sublistas = lista[1:3]
# print((sublistas))

"""comprobar si una lista contiene o no un elemento"""

# lista = ["dale", "un", "buen", "like", "crak"]
# palabra = "un"
# palabras = "auto"

# if palabra in lista:
#     print("la palabra esta en la lista")
    
# if palabras not in lista:
#     print("la palabra no esta en la lista")

"""modificar elementos de una lista"""

# lenguajes = ["java", "python", "c", "javaScript", "kitlin"]
# print((lenguajes))

"""como reemplazar un elemento de la lista"""
# lenguajes [1]= "angular"
# print(lenguajes)

"""como agregar un dato a un elemnto de la lista"""
# lenguajes[2] = lenguajes[2] + "++"
# print(lenguajes)

# lenguajes [2:4] = ["anaconda","typescritp"]
# print((lenguajes))

# lenguajes[1:2] = ["hola", "mundo", "soi" , "marcelo"]
# print((lenguajes))
    
"""METODOS DE LAS LISTAS: AÑADIR ELEMENTOS EN PYTHON PODEMOS UTILIZAR METODOS
CON LAS LISTAS""" 
# lenguajes = ["java", "python", "c", "javaScript", "kitlin"]

# lenguajes.insert(0, "c++")
# print((lenguajes))

# lenguajes.append("marcelo")
# print(lenguajes)

# lenguajesDos = ["hola", "mundo", "soi", "marcelo"]

# lenguajes.extend(lenguajesDos)
# print((lenguajes))

"""METODO DE ELIMINAR UN ELEMENTO DE LA LISTA"""

# frutas = ["paltano", "kiwi", "papaya", "melocoton", "cereza"]
# print(frutas)
# frutas.pop()
# print(frutas)

# frutas.pop(0)
# print(frutas)
# frutas.remove("kiwi")
# print(frutas)

# del frutas [0]
# print(frutas)

# indice = frutas.index("melocoton")
# print(indice)

"""crea una lista de 10 posiciones que contengas los numeros del 1 al 10"""

# lista = []
# for i  in range(10):
#     lista.append(i+1)
#     print(lista[i])

"""crea una tupla con valores ya predefinidos del 1 al 10, pide un indice por teclado  y 
muestra el valor de la tupla"""

# tuplas = (1.8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0.5)
# # print(tuplas)

# indice = int(input("dame un indice: "))
# print(tuplas[indice])

""" Supongamos un ejemplo en el que queremos construir una lista con los números pares del 1
al 20: """

even_numbers = []

def new_func(even_numbers):
    for i in range(20):
        if i % 2 == 0:
            even_numbers.append(i)
    print(even_numbers)

    # print(type(even_numbers))
    # print(dir(even_numbers))

new_func(even_numbers)

dias = ["lunes", "martes","miercoles"]
print(dias)