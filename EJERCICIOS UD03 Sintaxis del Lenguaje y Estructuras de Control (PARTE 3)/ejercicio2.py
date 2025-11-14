"""Calcular el perímetro y área de un rectángulo dada su base y su altura."""

base = float(input("Introduce la base del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))

perímetro = 2*(base+altura)
area = base*altura

print(f"Perímetro: {perímetro}, area: {area}")