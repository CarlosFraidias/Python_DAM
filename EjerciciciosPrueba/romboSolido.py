altura = int(input("introduce la altura"))

for i in range(altura):
    print(" "*(altura-1-i) + "*" * (2*i+1))
    
for i in range(1,altura):
    print(" " * i + "*" * (2*altura-2*i - 1))