"""Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura 
de la pirámide por teclado. Este es un ejemplo, si introducimos 5 de altura:"""

altura = int(input("Introduce la altura de la pirámide: "))

for i in range(altura):
    huecos = " " * (altura - 1 - i)
    asteriscos = "*" * (2 * i + 1)
    
    print(huecos + asteriscos)

