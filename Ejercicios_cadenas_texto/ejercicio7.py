"""Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena."""

resultado = ""

cadena = str(input("Introduce una cadena: "))

char1 = str(input("Introduce un caracter que quieras remplazar: "))
char2 = str(input("Ahora el remplazo: "))

for i in cadena:
    if i == char1:
        resultado = resultado + char2
    else:
        resultado = resultado + i
    
print(resultado)