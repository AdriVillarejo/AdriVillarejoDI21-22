import random

class ErrorEnterMassaGran(Exception):
    pass

class ErrorEnterMassaMenut(Exception):
    pass



numero= random.randint(0, 100)


i = 1

while (i == 1):
    valor = int(input("Introduzca un numero "))

    try:

        if numero < valor:
            raise ErrorEnterMassaGran
        
        if numero > valor:
            raise ErrorEnterMassaMenut

        else:
            print ("Has adivinado el número, enhorabuena!!")
            i = 0

    except ErrorEnterMassaGran:
        print ("El numero introducido es mayor al que tienes que adivinar, vuelve a intentarlo!")

    except ErrorEnterMassaMenut:
        print ("El numero introducido es menor al que tienes que adivinar, vuelve a intentarlo")    

    except ValueError:
        print ("Has introducido un caracter que no es un numero")
        break

        

        