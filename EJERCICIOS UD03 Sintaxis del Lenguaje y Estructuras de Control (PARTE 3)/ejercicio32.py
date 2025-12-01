"""La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro 
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los 
siguientes  tres,  80  céntimos,  los  siguientes  dos  minutos,  70  céntimos,  y  a  partir  del  décimo 
minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, 
en turno de mañana, 15 %, y en turno de tarde, 10 %.   
Realice un algoritmo para determinar cuánto debe pagar por cada concepto  una persona 
que realiza una llamada. """

minutos = float(input("Ingrese la duración de la llamada (en minutos): "))
dia = input("Ingrese el día de la semana (ej: domingo, lunes): ").lower()
turno = input("Ingrese el turno (mañana/tarde): ").lower()

costo = 0

if minutos <= 5:
    costo = 1
else:
    costo = 1
    minutos -= 5

    if minutos <= 3:
        costo += minutos * 0.80
        minutos = 0
    else:
        costo += 3 * 0.80
        minutos -= 3

        if minutos <= 2:
            costo += minutos * 0.70
            minutos = 0
        else:
            costo += 2 * 0.70
            minutos -= 2
 
            costo += minutos * 0.50
            
if dia == "domingo":
    impuesto = costo * 0.03
elif turno == "mañana":
    impuesto = costo * 0.15
else:  
    impuesto = costo * 0.10

total = costo + impuesto

print(f"\nCosto de la llamada (antes de impuestos): {costo:.2f} euros")
print(f"Impuesto aplicado: {impuesto:.2f} euros")
print(f"Total a pagar: {total:.2f} euros")