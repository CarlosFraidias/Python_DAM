"""Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares, 
con el siguiente menú de opciones: 

Bienvenido a su Cajero Virtual
    1. Ingresar dinero en cuenta
    2. Retirar dinero de la cuenta
    3. Salir"""
    
cuentaBanco = 0

while True:
    print("Bienvenido a su Cajero Virtual. Dinero en la cuenta:",cuentaBanco,"euros\n\t1. Ingresar dinero en cuenta\n\t2. Retirar dinero de la cuenta\n\t3. Salir")
    opcion = int(input("Introduce una opción: "))
    
    if opcion == 1:
        ingreso = float(input("Introduce el ingreso: "))
        cuentaBanco += ingreso
        print("Ingreso añadidio a la cuenta con éxito")
    elif opcion == 2:
        retirada = float(input("Cuánto dinero quieres retirar?"))
        if retirada > cuentaBanco:
            print("No tienes suficiente dinero en la cuenta.")
        else:
            cuentaBanco -= retirada
            print("Dinero retirado con éxito")
    elif opcion == 3:
        print("Saliendo del programa . . .")
        break
    else:
        print("Introduce una opción válida")
    
    print()

print("Fin del programa. Tu cuenta se quedó con",cuentaBanco, "euros")
        