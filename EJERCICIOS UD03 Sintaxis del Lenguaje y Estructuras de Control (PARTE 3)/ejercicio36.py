"""Escribe un programa que pida un número entero entre uno y doce e imprima el número de 
días que tiene el mes correspondiente. Si introducimos otro número nos da un error. """

mes = int(input("Introduce el mes en número: "))

meses31 = [1,3,5,7,8,10,12]
meses30 = [4,6,9,11]

if mes < 1 or mes > 12:
    print("Error.")
    exit()

if mes in meses30:
    print("Tiene 30 días.")
elif mes in meses31:
    print("Tiene 35 días.")
else:
    print("Tiene 28 dias o 29 si es bisiesto.")