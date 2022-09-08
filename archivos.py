# try:
#     with open("hola_mundo.txt") as file:
#         try:
#             file.write("hola")
#         except:
#             print("no pude escribir")
# except:
#     print("fallo")

"""LECTURA de un  archivo"""

# with open("hola_mundo.txt") as file:
#     print(file.read())
    # print(file.readlines())
# """ESCRITURA en un archivo"""

# with open("hola_mundo.txt","w") as file:
#     file.write("ian se porta mal muy mal\n")

# """AGREGAR  al archivo"""
# with open("hola_mundo.txt","a+") as file:
#     file.write("\n y va hacer castigado22")

"""COMO CREAR UN ARCHIVO"""

# archivo = open("archivo.txt","w")
# """AGREGAR AL ARCHIVO"""



"""COMO LEER Y ESCRIBIR EN UN ARCHIVO"""
with open("hola_mundo.txt","r+") as file:
    file.write("goro")
    print(file.read())

