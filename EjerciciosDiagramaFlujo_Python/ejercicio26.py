"""Dibuja un ordinograma que calcula el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
    • Las primeras 35 horas se pagan a tarifa normal.
    • Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
    • Las tasas de impuesto son:
    o Los primeros 500€ son libres de impuestos.
    o Los siguientes 400€ tiene un 25% de impuesto.
    o Los restantes un 45% de impuesto.
Escribe el nombre del trabajador, salario bruto, tasas y salario neto."""

nombre = input("Introduce el nombre del trabajador: ")
horas = int(input("Introduce las horas trabajadas en la semana: "))
tarifa = int(input("Introduce la tarifa del trabajador: "))

bruto = tarifa * horas

if horas>35:
    salarioBruto = (tarifa * 35) + (tarifa * (horas-35) * 1.5)
else:
    salarioBruto = tarifa * horas

if salarioBruto > 500:
    salarioNeto = 500
    salarioBruto -= 500
    if salarioBruto > 400:
        salarioNeto += 400 * 0.75
        salarioBruto -= 400
        salarioNeto += salarioBruto * 0.55

print("Nombre de trabajador:", nombre, "\nSalario bruto:", bruto, "\nSalario neto:", salarioNeto)
    
    