"""Leer una cadena y contar cuántas vocales contiene."""

cad = str(input("Introduce una cadena: "))

vocals = "aeiou"
contVocals = 0
for i in cad:
    if i in vocals:
        contVocals += 1

print("En la cadena habían", contVocals, "vocales")