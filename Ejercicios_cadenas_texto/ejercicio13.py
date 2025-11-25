"""Leer una cadena y eliminar todos los espacios, construyendo una cadena continua."""

cad = str(input("Introduce una cadena de texto para eliminar los espacios: "))
resultado = ""

for i in cad:
    if not (i == " "):
        resultado += i

print("Cadena sin espacios:",resultado)
        