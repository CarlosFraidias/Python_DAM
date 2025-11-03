"""Dibuja un ordinograma que dado el precio de un artículo y el precio de venta real nos
muestre el porcentaje de descuento realizado."""

precioArticulo = float(input("Introduce el precio del artículo: "))
precioVenta = float(input("Introduce el precio al cual se vendió el artículo: "))

desc = ((precioVenta/precioArticulo)-1)*(-100)
print("Se ha realizado un", format(desc,".2f"), "porciento de descuento")