"""Escriba un programa que recibe como datos de entrada una hora expresada en horas, 
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán, 
transcurrido un segundo."""
import time

while True:
    hora = int(input("Introduce la hora actual: "))
    min = int(input("Introduce los minutos: "))
    seg = int(input("Introduce los segundos: "))
    if (0 <= seg <= 59) and (0 <= min <= 59) and (0 <= hora <= 23):
        break
    print("Introduce los datos válidos.") 

#hago el bucle con el time.sleep para que parezca un reloj aunque no lo pide el ejercicio
while True:
    if seg == 59:
        seg = 0
        if min == 59:
            min = 0
            if hora == 23:
                hora = 0
            else:
                hora += 1
        else:
            min += 1
    else:
        seg += 1

    print(hora, "h ",min ,"min ", seg, "seg")
    time.sleep(1)