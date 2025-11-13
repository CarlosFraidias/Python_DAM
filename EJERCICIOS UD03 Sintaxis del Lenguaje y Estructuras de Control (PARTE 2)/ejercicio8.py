"""Programa que  lea 100 números no nulos y luego muestre un mensaje indicando cuántos 
son positivos y cuantos negativos."""

neg = 0
pos = 0
for i in range(0,100):
    print("numero", i)
    num = int(input("-Introduce un número:"))
    if num < 0:
        neg+=1
    else:
        pos+=1
        
print("Positivos:", pos, "\nNegativos:", neg)