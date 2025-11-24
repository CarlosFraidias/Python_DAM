"""Leer una cadena y construir una nueva cadena con los caracteres en orden inverso."""

result = ""

cad = str(input("Introduce una cadena para invertirla: "))

for i in range(len(cad), 0, -1):
    result = result + cad[i-1]

print(result)