"""Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez."""

vocales = "aeiou"

cad = str(input("Introduce una cadena para mostrar solo las consonantes: "))
result = ""
for i in cad:
    if not i in vocales:
        result += i
        
print(f"Cadena de solo consonantes: {result}")