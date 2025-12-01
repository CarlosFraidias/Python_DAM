"""Algoritmo que pida tres números y los muestre ordenados (de mayor a menor) """

n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))

"""Compruebo cual es el númeor mayor."""
numMayor = n1

if numMayor<n2:
    numMayor = n2
    
if numMayor < n3:
    numMayor = n3
    
"""Compruebo cual es el número menor"""
numMenor = n1

if numMenor>n2:
    numMenor = n2
    
if numMenor > n3:
    numMenor = n3
    
"""Compruebo el número intermedio"""

numInter = 0

if numMenor<=n1<=numMayor:
    numInter = n1
    
if numMenor<=n2<=numMayor:
    numInter = n2
    
if numMenor<=n3<=numMayor:
    numInter = n3
    
"""muestro resultados"""

print(f"{numMayor}, {numInter}, {numMenor}")
    

    
    
    
    
        


