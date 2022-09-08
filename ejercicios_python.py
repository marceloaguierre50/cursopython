def conversor(tipo_pesos,dolar):
    pesos = int(input(f"¿cuantos pesos {tipo_pesos} tienes?:"))
    valor_dolar = pesos / dolar
    valor_dolar = round(valor_dolar, 2)
    print(f"Tienes ${valor_dolar} dolar")

"""PROGRAMA DE CONVERSOR DE MONEDAS SIN FUNCIONES"""

# menu = """
# BIENVENIDOS AL PROGRAMA DE CONVERCION DE MONEDAD
# 1 - PESOS COLOMBIANOS 
# 2 - PESOS ARGENTINOS
# 3 - PESOS MEXICANOS

# ELIJE UNA OPCION : """
# opcion = int(input(menu))


# if opcion == 1 :
#     pesos = int(input("¿cuantos pesos colombianos tienes?:"))
#     dolar = 3875
#     valor_dolar = pesos / dolar
#     valor_dolar = round(valor_dolar, 2)
#     print(f"Tienes ${valor_dolar} dolar")
# elif opcion == 2:
#     pesos = int(input("¿cuantos pesos argentinos tienes?:"))
#     dolar = 330
#     valor_dolar = pesos / dolar
#     valor_dolar = round(valor_dolar, 2)
#     print(f"Tienes ${valor_dolar} dolar")
# elif opcion == 3 :
#     pesos = int(input("¿cuantos pesos mexicanos tienes?:"))
#     dolar = 383
#     valor_dolar = pesos / dolar
#     valor_dolar = round(valor_dolar, 2)
#     print(f"Tienes ${valor_dolar} dolar")
# else:
#     print("LA OPCION INGRESADA ES INCORRECTA\nPOR FAVOR IN GRESE NUEVAMENTE")

"""CONVERSOR DE MONEDAS CON FUNCIONES"""

# menu = """
# BIENVENIDOS AL PROGRAMA DE CONVERCION DE MONEDAD
# 1 - PESOS COLOMBIANOS
# 2 - PESOS ARGENTINOS
# 3 - PESOS MEXICANOS

# # ELIJE UNA OPCION : """
# opcion = int(input(menu))

# if opcion == 1 :
#     conversor("colombianos", 3785)
# elif opcion == 2:
#     conversor("argentionos", 300)
# elif opcion == 3 :
#     conversor("mexicanos", 345)
# else:
#     print("LA OPCION INGRESADA ES INCORRECTA\nPOR FAVOR IN GRESE NUEVAMENTE")

"""METODO RETURN REGRESAR  UN VALOR EN UNA FUNCION"""
# def suma (a , b):
#     print("la suma de dos numeros es:")
#     resultado = a + b
#     return resultado

# sumatoria = suma(1 , 2)
# print(sumatoria)

# """METODO upper() trasforma un caracter de minuscula a mayuscula"""
# nombre = input("ingrese nombre:")
# print(nombre)

# print(nombre.upper())
"""METODO capitalize() PONE LA PRIMERA LETRA EN MAYUSCULA"""
# print(nombre.capitalize())

"""METODO strip() PERMITE BORRAR ESPACIO"""
"""METODO lower() TRASNFORMA DE MAYUSCULA A MINUSCULA"""
"""METODO replace(a , o) REEMPLAZA LA LETRA A PO LA LETRA O"""
"""METODO len(parametro) PERMITE SABER LA LONGITUD DEL TEXTO"""
# print(nombre[0])
# print(len(nombre))

print("COMERCIO #######ROMAN#######")

productos ={"azucar": 10,
            "yerba":20,
            "sal" :30,
            "gomitas" : 40}
print(productos)
print(dir(productos))
print(type(productos))
# x = int(input("ingrese un numero:"))
# y = int(input("ingre otro numero:"))

# suma = x+y
# resta = x-y

# print(f"la suma es:{suma}")
# print(f"la resta es es :{resta}")
