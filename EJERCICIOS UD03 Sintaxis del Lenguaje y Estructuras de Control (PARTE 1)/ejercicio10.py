"""Dibuja un ordinograma que lea dos números, calcule y muestre el valor de sus suma, resta, 
producto y división (Ten en cuenta la división por cero)."""

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

print("suma:",num1+num2)
print("resta:",num1-num2)
print("multiplicación:",num1*num2)

if num2 == 0:
    print("división: no se puede dividir entre cero")
else:
    print("división:", num1/num2)