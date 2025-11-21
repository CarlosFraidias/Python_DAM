

while True:
    altura = int(input("Introduce la altura impar: "))
    if altura % 2 != 0:
        break
    
for i in range(altura):
    print(" " * (i) + "*" + " " * int(altura/3 -i) + "*" + " " * int(altura/3 -i) + "*")
