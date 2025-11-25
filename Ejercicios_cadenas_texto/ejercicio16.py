"""Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo)."""

cad1 = str(input("Introduce una cadena de texto: "))
cad2 = str(input("Introduce otra cadena de texto: "))

for i in cad2:
    cad1 += i

print("Cadena concatenada:", cad1)