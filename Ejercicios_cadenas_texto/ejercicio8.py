"""Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower())."""

mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minus = "abcdefghijklmnopqrstuvwxyz"
resultado = ""

cadena = input("Introduce una frase con mayúsculas y minúsculas: ")

opcion = int(input("Pasar a mayúsculas - 1\n"
                   "Pasar a minúsculas - 2\n"
                   "Introduce una opción: "))

if opcion == 1:   
    for i in cadena:
        if i in minus:
            resultado += chr(ord(i) - 32)
        else:
            resultado += i

elif opcion == 2:  
    for i in cadena:
        if i in mayus:
            resultado += chr(ord(i) + 32)
        else:
            resultado += i

print(resultado)
        

