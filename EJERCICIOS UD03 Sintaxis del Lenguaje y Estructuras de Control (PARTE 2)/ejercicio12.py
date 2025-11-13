"""Crea  una  aplicación  que  dibuje  una  escalera  de  números,  siendo  cada  línea  un  número. 
Nosotros le pasamos la altura por teclado."""

altura = int(input("Introduce la altura de la escalera: "))

num = 0

for i in range(0,altura):
    num += 1
    print(num)

