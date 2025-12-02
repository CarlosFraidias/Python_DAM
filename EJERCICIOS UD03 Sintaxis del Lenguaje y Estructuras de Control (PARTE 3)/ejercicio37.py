"""Una compañía de transporte internacional tiene servicio en algunos países de América del 
Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se 
basa en el peso del paquete y la zona a la que va dirigido... """

peso = float(input("Introduce el peso del paquete: "))
print("1- América del Norte\n2- América Central\n3- América del Sur\n4- Europa\n5- Asia")

opcion = int (input("Introduce una opcion: "))
costo = 0
match opcion:
    case 1: costo = peso * 11 
    case 2: costo = peso * 10 
    case 3: costo = peso * 12 
    case 4: costo = peso * 24 
    case 5: costo = peso * 27
    
print(f"Costo del paquete: {costo:.2f}$") 
    

