"""Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si 
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta” 
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo 
según sea el caso y el total a pagar de la compra."""

precio = float(input("Introduzca el valor de la compra: "))

opcion = int(input("1- al contado, 2- con tarjeta: "))

if opcion == 1:
    print("Se hará un descuento del 5%")
    precio = precio * 0.95
elif opcion == 2:
    print("Se añadirá un recargo de 3%")
    precio = precio * 1.03 

print("El total a pagar es:", format(precio, ".2f"))