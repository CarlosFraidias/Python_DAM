"""Dos  vehículos  viajan  a  diferentes  velocidades  (v1  y  v2)  y  están  distanciados  por  una 
distancia  d.  El  que  está  detrás  viaja  a  una  velocidad  mayor.  Se  pide  hacer  un  algoritmo  para 
ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto 
determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro. """

d = int(input("Distancia en km: "))
v1 = int(input("Velocidad 1 en km/h: "))
v2 = int(input("Velocidad 2 en km/h: "))

velocidad_relativa = v2 - v1

tiempo_horas = d / velocidad_relativa

tiempo_minutos = tiempo_horas * 60

print(f"Tiempo: {tiempo_minutos:.2f} minutos")
