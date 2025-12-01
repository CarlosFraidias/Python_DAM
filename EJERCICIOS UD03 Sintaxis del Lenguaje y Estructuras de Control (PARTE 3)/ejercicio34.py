"""Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta."""

dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

meses31 = [1,3,5,7,8,10,12]
meses30 = [4,6,9,11]

correcto = True

bisiesto = False
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            bisiesto = True
        else:
            bisiesto = False
    else:
        bisiesto = True

if 0<mes<13:
    if mes in meses31:
        if not 0<dia<=31:
            correcto = False
    elif mes in meses30:
        if not 0<dia<=30:
            correcto = False
    else:
        if bisiesto:
            if not 0<dia<=29:
                correcto = False
        else:
            if not 0<dia<=28:
                correcto = False
else:
    correcto = False
    
if correcto:
    print("La fecha introducida es correcta.")
else:
    print("La fecha introducida es incorrecta.")