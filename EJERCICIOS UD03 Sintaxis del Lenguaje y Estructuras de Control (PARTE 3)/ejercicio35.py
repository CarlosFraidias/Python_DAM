"""Realiza un programa que pida el dí-a de la semana (del 1 al 7) y escriba el día 
correspondiente. Si introducimos otro número nos da un error."""

dia = int(input("Introduce el dia de la semana en números: "))
cad = ""

if dia < 1 or dia > 7:
    print("Error.")
    exit()

match dia:
    case 1: cad = "lunes"
    case 2: cad = "martes"
    case 3: cad = "miércoles"
    case 4: cad = "jueves"
    case 5: cad = "viernes"
    case 6: cad = "sábado"
    case 7: cad = "domingo"
    
print(f"Día de la semana: {cad}")  