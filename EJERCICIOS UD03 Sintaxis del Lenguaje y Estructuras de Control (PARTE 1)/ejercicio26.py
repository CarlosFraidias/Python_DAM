"""En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido 
en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
    Si los tres dados son seis, mostrar el mensaje “Excelente”
    Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
    Si un dado se obtiene seis, mostrar el mensaje “Regular”
    Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
(Use el control switch).""" 

import random, time


num6 = 0

print("A continuación se tirarán tres dados\nDependiendo de cuantos 6 hayas obtenido tendras una puntuación distinta")

for i in range(0,3):
    time.sleep(2)
    dado = random.randint(1,6)
    print("Dado número", i+1, "-", dado)
    if dado == 6:
        num6 += 1


match num6:
    case 0:
        print("Pésimo")
    case 1:
        print("Regular")
    case 2:
        print("Muy bien")
    case 3:
        print("Excelente")

print("Fin del programa")

    