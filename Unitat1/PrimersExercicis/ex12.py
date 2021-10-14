import os

from sys import is_finalizing

base_url= os.path.dirname(__file__)

try: 

    z = open(os.path.join(base_url, "prueba.txt"), "r")

except FileNotFoundError:

    print ("No se ha encontrado el fichero!")

try: 

    ficherocreado = open(os.path.join(base_url, "crearfichero.txt"), "w")

except FileNotFoundError:

    print ("No se ha encontrado el fichero!")

suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplicacion = lambda x, y: x * y
division = lambda x, y: x / y

for i in z:

    numstring = i.split(" ")

    if (numstring[1] == "+"):
        try: 
            resultado = suma(int(numstring[0]), int(numstring[2]))
            print(numstring[0], " ", numstring[1], " ", int(numstring[2]), " = ", resultado)
        except ValueError:
            "En el fichero tienen que haber números!"

    if (numstring[1] == "-"):
        try:

            resultado = resta(int(numstring[0]), int(numstring[2]))
            print(numstring[0], " ", numstring[1], " ", int(numstring[2]), " = ", resultado)
        except ValueError:
            "En el fichero tienen que haber números!"

    if (numstring[1] == "*"):
        try:

            resultado = multiplicacion(int(numstring[0]), int(numstring[2]))
            print(numstring[0], " ", numstring[1], " ", int(numstring[2]), " = ", resultado)
        except ValueError:
            "En el fichero tienen que haber números!"

    if (numstring[1] == "/"):
        try:

            resultado = division(int(numstring[0]), int(numstring[2]))
            print(numstring[0], " ", numstring[1], " ", int(numstring[2]), " = ", resultado)
        except ValueError:
            "En el fichero tienen que haber números!"

        except ZeroDivisionError:
            "No se puede dividir entre 0 :)"


z.close(    )
