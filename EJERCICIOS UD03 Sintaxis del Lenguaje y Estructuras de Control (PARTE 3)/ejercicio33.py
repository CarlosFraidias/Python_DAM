"""Realiza un programa que pida por teclado el resultado (dato entero) obtenido  al lanzar un 
dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta 
al resultado obtenido. 
Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4. 
Nota 2: Si el número del dado introducido es menor que  1 o mayor que 6, se mostrará el 
mensaje: "ERROR: número incorrecto."""

dado = int(input("Introduce el número del dado: "))

cad = ""

if 1>= dado or dado >= 6:
    print("ERROR: número incorrecto.")
    exit()

match dado:
    case 1: 
        cad = "seis"
    case 2:
        cad = "cinco"
    case 3:
        cad = "cuatro"
    case 4: 
        cad = "tres"
    case 5:
        cad = "dos"
    case 6:
        cad = "uno"
        
print(f"Dato en cadena: {cad}")