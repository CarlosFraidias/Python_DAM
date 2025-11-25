"""Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez."""

repetidos = ""
caracteresDuplicados = ""


cad = str(input("Introduce una cadena para mostrar solo los caracteres repetidos de la misma: "))

for i in cad:
    if not i in repetidos:
        repetidos += i
    else:
        if not i in caracteresDuplicados:
            caracteresDuplicados += i
        
print(f"Caracteres duplicados: '{caracteresDuplicados}'")