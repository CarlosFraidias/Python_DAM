"""Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos 
la altura de la pirámide por teclado. Este es un ejemplo:"""

altura = int(input("Introduce la altura de la piramide: "))

for i in range(altura):
    asteriscos = "*" * (2*(altura-i)-1)
    huecos = " " * (i)
    print(huecos + asteriscos)