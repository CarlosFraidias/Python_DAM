"""Dibuja un ordinograma que lea una calificación numérica entre 0 y 10 y la transforme en la
calificación alfabética, escribiendo el siguiente resultado.
    • De 0 a < 3 Muy Deficiente.
    • De 3 a < 5 Insuficiente.
    • De 5 a < 6 Suficiente.
    • De 6 a < 7 Bien.
    • De 7 a <9 Notable.
    • De 9 a 10 Sobresaliente"""
    
    
while True:
    nota = float(input("Introduce la nota numérica entre 0 y 10: "))
    if nota >= 0 and nota <= 10:
        break

notaAlfabetica = ""
if nota < 3:
    notaAlfabetica = "Muy deficiente"
elif 3<= nota < 5:
    notaAlfabetica = "Insuficiente"
elif 5<= nota < 6:
    notaAlfabetica = "Suficiente"
elif 6<= nota < 7:
    notaAlfabetica = "Bien"
elif 7<= nota < 8:
    notaAlfabetica = "Notable"
elif 9<= nota:
    notaAlfabetica = "Sobresaliente"
    
print("La nota del alumno fué:", notaAlfabetica)