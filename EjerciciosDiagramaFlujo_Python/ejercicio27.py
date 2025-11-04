"""Dibuja un ordinograma de un programa que lea una secuencia de notas (con valores que
van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10."""

nota = int(input("Introduce una nota, -1 para finalizar: "))
diez = False
while nota != -1:
    if nota == 10:
        diez = True
    nota = int(input("Introduce una nota, -1 para finalizar: "))


if diez:
    print("Ha habido algun diez")
    
print("Fin del programa")