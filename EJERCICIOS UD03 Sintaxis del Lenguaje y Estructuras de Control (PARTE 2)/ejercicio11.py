"""Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de 
la escalera por teclado. Este es un ejemplo si insertaras un 5 de altura: """

asteriscos = ""

altura = int(input("Introduce la altura de la pirámide: "))

for i in range(altura):
    asteriscos += '*'
    print(asteriscos)