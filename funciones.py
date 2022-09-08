
def suma(num1,num2):
    return(num1+num2)

"""COMO CONCATENAR UN STRIN CON UN ENTERO"""
print(f"la suma es :{suma(4,3)}")
print("la suma es: " + str (suma(3,3)))

def potencia (nu1,nu2):
    return(nu1**2+nu2**2)

print(f"la potencia es:{potencia(3,4)}")

def factor (n):
    return(n*4*3*2*1)
print(factor(5))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))

"""Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un
 muy buen ejercicio."""
 
# n1 = input("ingrese el primer numero:")
# n2 = input("ingrese el segundo numero:")

# def marce (n1, n2):
#     if n1 < n2:
#         print("el numero mas grande es:")
#         print (n2)
#     elif n2 < n1:
#         print("el numero mas grande es:")
#         print (n1)
#     else:
#         print ("Son iguales")
# print(type(marce))
    
# marce(2,1)

"""Definir una función max_de_tres(), que tome tres números como argumentos y 
devuelva el mayor de ellos."""

# def maximo (n1,n2,n3):
#     if n1 > n2 and n1 > n3:
#         print(n1)
#     elif n2>n1 and n2>n3:
#         print(n2)
#     else:
#         print(n3)
        
        
# maximo(30,30, 30)

"""Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, pero escribirla por 
 nosotros mismos resulta un muy buen ejercicio."""
 
def largo_cadena (lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont
print (largo_cadena("hola"))
print (largo_cadena([2,7,8]))


# def hola ():
#     print("hola")
#     print("estoi aprendiendo a usar funciones")
#     print("mensaje especial")

def conversacion (mensaje):
    print("hola")
    print("estoi aprendiendo a usar funciones")
    print(mensaje)
    print("adios")

opcion = int(input("hola elige una opcion: 1 , 2, 3:"))

if opcion == 1:
    conversacion("lejiste la opcion 1")
elif opcion == 2:
    conversacion("elejiste la opcion 2")
elif opcion == 3:
    conversacion("elejiste la opcion 3")
else:
    print("la opcion ingresada es incorrecta")
    
def suma(x,y):
    suma= x+ y
    print(suma)




# hola()
# hola()
# hola()