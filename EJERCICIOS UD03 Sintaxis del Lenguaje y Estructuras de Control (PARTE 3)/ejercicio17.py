"""Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.  El tiempo de 
viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora 
de llegada a la ciudad B."""

horas = int(input("Introduce la hora de salida del ciclista: "))
minutos = int(input("Introduce los minutos de salida del ciclista: "))
segundos = int(input("Introduce los segundos de salida del ciclista: "))
t = int(input("Introduce en segundos el tiempo que tardará el ciclista en llegar a la otra ciudad: "))

for i in range(t):
    if segundos == 59:
        segundos = 0
        if minutos == 59:
            minutos = 0
            if horas == 23:
                horas = 0
            else:
                horas += 1
        else:
            minutos +=1
    else:
        segundos+=1
        
print(f"{horas}h {minutos}min {segundos}seg")
    