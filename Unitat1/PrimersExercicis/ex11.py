import os

from sys import is_finalizing

base_url= os.path.dirname(__file__)

z = open(os.path.join(base_url, "prueba.txt"), "r")


ficherocreado = open(os.path.join(base_url, "crearfichero.txt"), "w")

suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplicacion = lambda x, y: x * y
division = lambda x, y: x / y

for i in z:

    numstring = i.split(" ")

    if (numstring[1] == "+"):
        resultado = suma(int(numstring[0]), int(numstring[2]))
        print(numstring[0], " ", numstring[1], " ", int(numstring[2]), " = ", resultado)
    if (numstring[1] == "-"):
        resultado = resta(int(numstring[0]), int(numstring[2]))
        print(numstring[0], " ", numstring[1], " ", int(numstring[2]), " = ", resultado)
    if (numstring[1] == "*"):
        resultado = multiplicacion(int(numstring[0]), int(numstring[2]))
        print(numstring[0], " ", numstring[1], " ", int(numstring[2]), " = ", resultado)
    if (numstring[1] == "/"):
        resultado = division(int(numstring[0]), int(numstring[2]))
        print(numstring[0], " ", numstring[1], " ", int(numstring[2]), " = ", resultado)

z.close()
