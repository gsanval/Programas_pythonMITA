# Calcula el area de un circulo dado el radio

import math  #Libreria para las funciones y constantes matematicas

print("Calculando el area de un circulo\n")

radio = float(input("Dame el radio: "))
# area = 3.1416 *radio *radio
area = math.pi * math.pow(radio,2)

print(f"El area es {area:.2f}")

