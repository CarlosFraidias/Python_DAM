"""Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el 
vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas 
que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y 
comisiones."""

sueldoBase = float(input("Introduce el sueldo base del trabajador: "))
dineroVentas = float(input("Introduce el monto general de ventas del mes"))

comisionVentas = dineroVentas * 0.1

total = (sueldoBase + comisionVentas)

print(f"El sueldo total del trabajador es: {total}")