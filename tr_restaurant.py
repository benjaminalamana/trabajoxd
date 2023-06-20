
import os
import time
import msvcrt
import numpy

arreglo_restorant = numpy.zeros((3,3),int)
def validar_opcioin():
    while True:
        try:
            opcion = int(input("ingerse opcion: "))
            if opcion in (1,2,3,4,5,6):
                return opcion
            else:
                print("ERROR OPCION INCORRECTA ")
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO")


def ver_restaurant():
    print(" VER SALON PRINCIPAL")
    print("                     ")
    print("                     ")
    print("                     ")  
    print("                     ")
    for x in range(3):
            print(f"Fila {x+1}:\t" , end="")
            for y in range(3):
                print(arreglo_restorant[x][y], end=" ")
            print()
    print("        1 2 3 ")
    print("       COLUMNAS")
    print("")
    print("")
    print("")
    
def reservar_mesa():
    pass

def carta():
    while True:
        int(input(""))

def pagar():
    pass
def cancelar():
    pass
def salir ():
    pass

while True:
    print("""   menú
    1. ver restaurant
    2. reservar mesa 
    3. carta
    4. pagar
    5. cancelar
    6.salir""")

    opcion = validar_opcioin()
    if opcion ==1:
        ver_restaurant()
    elif opcion ==2:
        pass
    elif opcion ==3:
        pass
    elif opcion ==4:
        pass
    elif opcion ==5:
        pass
    else:
        break