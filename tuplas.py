"""son objetos inmutables quiere decir que sus elementos no pueden ser modificados"""

# tuplas = (1, "hola", 10.5)

# print(tuplas)

# print(type(tuplas))
# print(tuplas[2])

# tuplas [0] = "hola"
# print(tuplas)

""""crea una tuplas con los meses del año, despues pide un numero  entre 1 y 12 y muestre el
mes que corresponde, hasta que el usuario no meta un 0 el programa no termina"""



meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
        "septiembre", "obtubre", "noviembre", "diciembre")
# print(meses)

# mes = 1
# while mes!=0:
#     mes = int(input("ingrese un numero entre 1 y 12:"))
#     if (mes >=1 and mes <=12):
#         print(meses[mes-1])

"""Asigna un valor entero 2001 a la variable space_odyssey y muestra su valor."""

# space_adyssey = 2001

# print(space_adyssey)

"""Asigna la expresión 10 * 3.0 a la variable result y muestra su tipo."""   
# resul = 10 * 3.0

# print(resul)
# print(type(resul))

"""Escriba un programa en Python que acepte el radio de un círculo y compute su área"""
"""el .format() te permite concatenar un str con un int osea un numero con una 
cadena de texto"""

# pi = 3.14
# radio = (int(input("ingrese el radio:")))
# area = pi * radio**2
# print("el area del circulo es: {}" .format(area))

"""Escriba un programa en Python que acepte la base y la altura de un triángulo y
compute su área"""

# base = (int(input("ingrese la base de un triangulo:")))
# altura = (int(input("ingrese la altura de un triangulo:")))

# area = (base * altura / 2)

# print("el area del triangulo es: {}" .format(area))

"""Escriba un programa en Python que compute el futuro valor de una cantidad de dinero,
a partir del capital inicial, el tipo de interés y el número de años 
Entrada: capital=10000; interés=3.5; años=7
Salida: 12722.792627665729"""

# interes = 3.5
# años = 7

# entrada = (int(input("ingrese capital:")))

# capital = (entrada * interes * años)

# print("el capital en 7 años sera de : {}" .format(capital))

"""Escriba un programa en Python que lea por teclado dos números enteros y muestre por
pantalla el resultado de realizar las operaciones básicas entre ellos."""

# x = int(input("ingrese un numero:"))
# y = int(input("ingrese un numero:"))

# suma = (x + y)
# resta = ( x - y)
# multiplicacion = ( x * y)
# divicion = (x / y)

# print("la suma es: {}" .format(suma))
# print("la resta es : {}" .format(resta))
# print("multiplicacion es: {}" .format(multiplicacion))
# print("la divicion es: {}" .format(divicion))


# name = "marcelo"
# edad = 32
# fortuna = 100000

# print(f"me llamo {name} y tengo {edad} y mi fortuna es de {fortuna} millones ")


"""La función chr() permite representar un carácter a partir de su código:"""
# rocket_code = 0x1F680
# rocket = chr(rocket_code)
# print(rocket)

"""Ejercicio
Escriba un programa que permita adivinar un personaje de Marvel en base a las tres
""preguntas siguientes:"""
"""1. ¿Puede volar?
2. ¿Es humano?
3. ¿Tiene máscara?"""

# print("=============================================================")
# print("VAMOS A JUGAR UN JUEGO ADIVINARE TU PERSONAJE DE MARVEL")
# print("=============================================================\n")


# puede_volar = input("Tu personaje puede volar:")
# es_humano = input("Tu personaje es humano:")
# usa_mascara = input("Tu personaje usa mascara:")

# personaje = "si"
# personaje = "no"

# if puede_volar == "si":
#     if es_humano == "si":
#         if usa_mascara == "si":
#             print("TU PERSONAJE ES :iroman")
#         else:
#             print("TU PERSONAJE ES :capitan marvel")
#     elif usa_mascara == "no":
#         print("vision")
#     else:
#         print("ronan")

# else:
#     if puede_volar == "no":
#         if es_humano == "no":
#             if usa_mascara == "no":
#                 print("TU PERSONAJE ES:thanos")
#             else:
#                 print("TU PERSONAJE ES :black bolt")
#         elif usa_mascara == "si":
#             print("spiderman")
#         else:
#             print("hullk")
"""Escriba un programa en Python que pida (por separado) dos valores numéricos y un operando
(suma, resta, multiplicación, división) y calcule el resultado de la operación, usando para ello
la sentencia match-case.
Controlar que la operación no sea una de las cuatro predefinidas. En este caso dar un mensaje
de error y no mostrar resultado final.
Ejemplo
• Entrada: 4, 3, +
• Salida: 4+3=7"""

# x = int(input("ingrese un valor:"))
# y = int(input("ingrese segundo valor:"))
# operando = input("ingrese un operando:")
# suma = x + y
# resta = x -y
# multiplicacion = x*y
# divicion = x / y

# if operando == "suma":
#     print(suma)
# else:
#     if operando == "resta":
#         print(resta)
#     else:
#         if operando == "multiplicacion":
#             print(multiplicacion)
#         else:
#             print(divicion)

"""COMO SACAR LA RAIZ CUADRA DE UN NUMERO"""

# import math

# x = 16
# y = math.sqrt(x)
# print(y)

