"""Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'."""

cad = str(input("Introduce una cadena para sustituir los espacios por asteriscos: "))

result = ""
for i in cad:
    if i == " ":
        result += "*"
    else:
        result += i
        
print("La nueva cadena es:", result)