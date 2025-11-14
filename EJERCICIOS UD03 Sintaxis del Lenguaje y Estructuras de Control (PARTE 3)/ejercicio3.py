"""Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. """

import math

cat1 = float(input("Introduce un cateto del triángulo"))
cat2 = float(input("Introduce el otro cateto del triángulo"))

hip = math.sqrt(cat1**2 + cat2**2)

print(f"La hipotenusa es: {hip}")