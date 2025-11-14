"""Programa que dada una cantidad de euros que el usuario introduce por teclado (múltiplo de 
5 €) mostrará los billetes de cada tipo que serán necesarios para alcanzar dicha cantidad 
(utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar el mínimo de billetes posible. 
Por ejemplo, si el usuario introduce 145 el programa indicará que será necesario 1 billete de 100 
€, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo 29 billetes de 5, que aunque 
sume 145 € no es el mínimo número de billetes posible)."""

print("A continuacion introduce la cantidad de dinero que quiere recoger, para ver los billetes necesarios que se le darán\nEl dinero deberá ser múltiplo de 5 obligatoriamente")

while True:
    dinero = int(input("Introduce el dinero múltiplo de 5"))
    if dinero % 5 == 0:
        break

bill500, bill200, bill100, bill50, bill20, bill10, bill5 = 0,0,0,0,0,0,0

while dinero >= 500:
    dinero = dinero - 500
    bill500 += 1
    
while dinero >= 200:
    dinero = dinero - 200
    bill200 += 1

while dinero >= 100:
    dinero = dinero - 100
    bill100 += 1
    
while dinero >= 50:
    dinero = dinero - 50
    bill50 += 1
    
while dinero >= 20:
    dinero = dinero - 20
    bill20 += 1
    
while dinero >= 10:
    dinero = dinero - 10
    bill10 += 1
    
while dinero >= 5:
    dinero = dinero - 5
    bill5 += 1
    
print("Estos son los billetes necesarios:\n\nBilletes de 500:", bill500, "\nBilletes de 200:", bill200, "Billetes de 100:", bill100, "\nBilletes de 50:", bill50,"\nBilletes de 20:", bill20, "\nBilletes de 10:", bill10,"\nBilletes de 5:", bill5)
    
