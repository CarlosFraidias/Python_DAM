"""Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas)."""

resultado = ""

entrada = str(input("Introduce una cadena de caracteres: "))

for i in entrada:
    resultado = resultado + i

print(resultado)

