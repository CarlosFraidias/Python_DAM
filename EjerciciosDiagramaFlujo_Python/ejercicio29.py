"""Dibuja un ordinograma de un programa donde el usuario “piensa” un número del 1 al 100 
y el ordenador intenta adivinarlo. Es decir, el ordenador irá proponiendo números una y otra 
vez hasta adivinarlo (El usuario deberá indicarlo al ordenador si es mayor o menor o igual al 
número pensado)."""

import random
import time
print("Piensa en un número del 1 al 100, el programa tratara de adivinarlo.\nTu debes imdicarle al programa si el número sugerido es mayor menor o igual con los simbolos < , > , =")
time.sleep(2)
adivinado = False
primerNum = 1
ultimoNum = 100


while not adivinado:
    num = random.randint(primerNum , ultimoNum)
    print("Sistema- Tu número es", num,"?")
    opcion = (input("Introduce si es mayor>, menor<, o igual=."))
    
    if opcion == '>':
        primerNum = num+1
    elif opcion == '<':
        ultimoNum = num-1
    elif opcion == '=':
        adivinado = True
    else:
        print("Introduce una opción correcta")

print("Sistema- He adivinado tu número:", num, "\nFin del programa")