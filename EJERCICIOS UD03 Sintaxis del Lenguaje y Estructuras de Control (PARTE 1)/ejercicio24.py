"""Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día 
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra. 
Visualizar el descuento y el total a pagar por la compra. """

diasDeLaSemana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

monto = float(input("Introduce el monto de compra: "))
while True:
    dia = input("Ahora el dia de hoy: ").strip().lower()
    if dia in diasDeLaSemana:
        break
    print("Introduce un día de la semana válido")

if dia == "martes" or dia == "jueves":
    print("15%","de descuento")
    monto = monto * 0.85

print("El total a pagar es:", format(monto, ".2f"))
    