"""Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos 
la altura de la pirámide por teclado. Este es un ejemplo:"""

altura = int(input("Introudce la altura de la piramide"))

for i in range(altura):
    asteriscos = "*" * (2*(altura -1 -i))
    hecos = " " * (i)
    print(asteriscos + hecos)