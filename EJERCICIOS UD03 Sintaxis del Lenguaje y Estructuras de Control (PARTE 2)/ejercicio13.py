"""Crea  una  aplicación  que  dibuje  una  escalera  de  números,  siendo  cada  línea  números 
empezando en uno y acabando en el numero de la línea. Este es un ejemplo, si introducimos un 
5 como altura:"""

altura = int(input("Introduce la altura de la escalera: "))

num = 0
linea = ""

for i in range(0,altura):
    num += 1
    linea += str(num) + " "
    print(linea)