"""Dado  un  número  de  dos  cifras,  diseñe  un  algoritmo  que  permita  obtener  el  número 
invertido. """

while True:
    num = int(input("Introduce un número de dos cifras: "))
    if(num<100 and num>9):
        break
    print("Introduce un número de dos cifras por favor.")
    
inverted = (num%10) * 10
inverted = inverted + num//10

print(f"Inverso: {inverted}")    
