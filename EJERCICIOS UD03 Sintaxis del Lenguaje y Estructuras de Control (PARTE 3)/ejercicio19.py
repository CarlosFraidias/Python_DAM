"""Escribir  un  algoritmo  para  calcular  la  nota  final  de  un  estudiante,  considerando  que:  por 
cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime 
el resultado obtenido por el estudiante."""
import random
calificacion = 0

print("EXAMEN DE MULTIPLICACIÓN")

for i in range(1,21):
    prod1 = random.randint(1,10)
    prod2 = random.randint(1,10)
    
    respuesta = str(input(f"{prod1} * {prod2} = "))
    
    if respuesta == str(prod1*prod2):
        calificacion += 5
        print("Correcto +5")
    elif respuesta == "":
        calificacion = calificacion
        print("Sin responder +0")
    else:
        calificacion -= 1
        print("Incorrecto -1")
        
if calificacion < 0:
    calificacion = 0
    
print(f"Resultado del estudiante: {calificacion}/100")