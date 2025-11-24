"""Verificar si un carácter específico está en la cadena con un ciclo y comparaciones."""

caracter = 'a'

entrada = str(input("Introduce una frase: "))

contiene = False
for i in entrada:
    if i == caracter: 
        contiene = True

if contiene:
    print("La frase contiene el caracter", caracter)
else:
    print("La frase no contiene el caracter", caracter)