"""Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene."""

num = "123456789"

cad = str(input("Introduzca una cadena de caracteres para ver cuantos carácteres numéricos contiene: "))

contNum = 0
for i in cad:
    if i in num:
        contNum+=1

print("En la cadena introducida se encontró", contNum, "carácteres numéricos.")