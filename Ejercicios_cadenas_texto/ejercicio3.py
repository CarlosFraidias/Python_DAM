"""Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador."""

cad = str(input("Introduce una cadena de texto: "))
caracter = str(input("Introduce un caracter que quieras contar de tu cadena: "))

cont = 0
for i in cad:
    if i == caracter:
        cont += 1
        
print(f"Han habido {cont} caracteres '{caracter}' en la cadena introducida")