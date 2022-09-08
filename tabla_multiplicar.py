# for i in range(1, 3):
#     for j in range(1, 11):
#         result = i * j
#         print(f"{i} * {j} = {result}")

def calculo (x , y ,operacion):
    if operacion == "suma":
        suma = x + y
        print(f"la suma es: {suma}")
        return "GRACIAS ADIOS"
    elif operacion == "resta":
        resta = x -y
        print(f"la resta es:{resta}")
        return "GRACIAS ADIOS"
    elif operacion == "multiplicacion":
        multiplicacion = x *y
        print(f"la multiplicacion es:{multiplicacion}")
        return "GRACIAS ADIOS"
    else:
        division = x / y
        print(f"la divicion es:{division}")
        return "GRACIAS ADIOS"

menu = """bienvenidos al programa de operaciones
1-- << suma>>
2-- <<resta>>
3-- <<multiplicacion>>
4-- <<divicion>>
ELIJA UNA OPCION:"""
x = int(input("ingrese un numero:"))
y = int(input("ingrese segundo valor:"))
operacion= str(input(menu))

if operacion == "suma":
    print(calculo (x,y,operacion))
elif operacion == "resta":
    print(calculo(x,y,operacion))
elif operacion == "multiplicacion":
    print(calculo(x,y,operacion))
elif operacion == "divicion":
    print(calculo(x,y,operacion))
else:
    print("""<<<ERROR>>> INGRESASTE UNA OPCION INCORECTA ADIOS""")






# print(calculo(5,5,"suma"))
# print(calculo(2,2,"resta"))
