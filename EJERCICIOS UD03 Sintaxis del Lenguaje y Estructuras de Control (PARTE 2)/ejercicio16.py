"""Programa que lee una secuencia de notas (con valores que van de 0 a 10) que termina con 
el valor -1 y nos dice si hubo o no alguna nota con valor 10."""

notaDiez = False

while True:
    nota = float(input("Introduce la nota: "))
    if(nota == 10):
        notaDiez = True
    if(nota == -1):
        break

if notaDiez:
    print("Ha habido algún diez")
else:
    print("No ha habido ningún diez")
    
print("Fin del programa")
    