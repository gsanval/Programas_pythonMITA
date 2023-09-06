# Calculcar la hipotenusa de un triangulo dadas las longitudes de sus lados

import math

print("Calculcar la hipotenusa de un triangulo dadas las longitudes de sus lados\n")
longitud1, longitud2 = float(input()), float(input())
hipotenusa = math.sqrt( longitud1 * longitud1 + longitud2 * longitud2 )

print(f"La hipotenusa es {hipotenusa:.2f}")
