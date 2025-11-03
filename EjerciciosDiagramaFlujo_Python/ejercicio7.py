"""Dibuja un ordinograma que lea un valor correspondiente a una distancia en millas marinas
y escriba la distancia en metros. Sabiendo que una milla marina equivale a 1.852 metros."""

millas = float(input("Introduce una distancia en millas marinas: "))
metros = millas*1.852
print("Metros:",format(metros,".2f"))