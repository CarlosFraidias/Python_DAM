
altura = int(input("Introduce la altura: "))


for i in range(altura - 1):
    if i == 0:
        linea = ((" " * (altura -1-i) )+("*")+(" "*(i-1)))
    else:
        linea = ((" " * (altura  -1-i) )+("*")+(" "*(i-1))+("*"))
    print(linea)
    
print("*" + (" " * (altura -2) + "*"))

for i in range(altura - 1):
    if i == altura-2:
        linea = (" " * (i+1)) + ("*") + (" " * (altura -i -3))
    else:
        linea = (" " * (i+1)) + ("*") + (" " * (altura -i -3)) + ("*")
    
    print(linea)
    