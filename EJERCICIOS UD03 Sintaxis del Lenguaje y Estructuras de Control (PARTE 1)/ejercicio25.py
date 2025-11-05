"""La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el 
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre 
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el 
control switch)."""
print("Facultades disponibles: \n\ting de sistemas\n\tderecho\n\ting naviera \n\ting pesquera\n\tcontabilidad\n\tadministracion")


nombre = input("Introduce el nompre del postulante: ")

facultad = input("Introduce la facultad que va a estudiar").strip().lower()

mensualidad = 0
importe = 0

match facultad:
    case "ing de sistemas":
        importe = 350
        menusalidad = 650
    case "derecho":
        importe = 300
        menusalidad = 550
    case "ing naviera":
        importe = 300
        menusalidad = 500
    case "ing pesquera":
        importe = 310
        menusalidad = 460
    case "contabilidad":
        importe = 280
        menusalidad = 490
    case "administracion":
        importe = 360
        menusalidad =520
    case _:
        print("facultas no válida")
        exit()
        
igv = (mensualidad + importe) * 0.18
total = importe + mensualidad + igv

print("\n--- BOLETA DE MATRÍCULA ---")

print("Postulante:", nombre)
print("Facultad: ", facultad)
print("Importe de la matrícula:", importe)
print("Mensualidad:", mensualidad)
print("IGV:", igv)
print("Monto final a pagar:", total)