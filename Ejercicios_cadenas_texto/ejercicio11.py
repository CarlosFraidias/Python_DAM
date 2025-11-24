"""Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal."""

vocales = "aeiou"
result = ""
cad = str(input("Introduce una cadena para duplicar sus vocales"))

for i in cad:
    if i in vocales:
        result = result + i*2
    else:
        result = result + i

print(result)
