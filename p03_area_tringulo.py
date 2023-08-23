# Calcula el area de un trinagulo dada la base y la altura

import math

print("Calculando el area de un triangulo\n")

print("Dame la base y la altura separados por un enter\n")

base, altura = int(input()), int(input())
area = (base * altura)/2

print(f"El area del triangulo es igual a {area:.2f}")

