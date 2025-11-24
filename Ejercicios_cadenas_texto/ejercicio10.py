"""Leer una cadena y contar cuántos caracteres son letras mayúsculas."""

mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cad = str(input("Introduce una frase para contar sus mayusculas: "))
contMayus = 0
for i in cad:
    if i in mayus:
        contMayus += 1

print("En la cadena han habido", contMayus, "mayúsculas")