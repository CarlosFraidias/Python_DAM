altura = int(input("Introduce la altura: "))
print(" " * (altura-1) + "*")
for i in range(altura-2):
    print((" "* (altura-2-i)) + "*" + (" " * (2*i +1)) + "*")
    
print("*" + " " * (altura*2-3) + "*")

for i in range(altura-2):
    print((" ")*(i+1) + "*" + " " * (altura-2*i) + "*")
    
print(" " * (altura-1) + "*")

