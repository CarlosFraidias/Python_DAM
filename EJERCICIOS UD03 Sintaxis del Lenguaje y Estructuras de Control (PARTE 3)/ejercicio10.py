"""Un alumno desea saber cuál será su calificación final en la materia de Algoritmos Dicha 
calificación se compone de los siguientes porcentajes:
    • 55% del promedio de sus tres calificaciones parciales.
    • 30% de la calificación del examen final.
    • 15% de la calificación de un trabajo final."""
    
califParciales = [0,0,0]

for i in range(0,3):
    califParciales[i] = float(input(f"Introduce la nota del parcial {i+1}: "))

examFinal = float(input("Introduce la nota del examen final: "))
trabajoFinal = float(input("Introduce la nota del trabajo final: "))


promedioParcial = 0
for i in califParciales:
    promedioParcial += i

promedioParcial = promedioParcial/len(califParciales)

califFinal = (promedioParcial*0.55) + (examFinal*0.30) + (trabajoFinal*0.15)

print(f"La calificación final es. {califFinal}")

