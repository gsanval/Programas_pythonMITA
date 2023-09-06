# Calcular el volumen de un cilindro dado su radio y altura
import math

print("Calculando el volumen de un cilindro\n")
print("Dame el radio y la altura:")
radio, altura = float(input()), float(input())
volumen = math.pi * (math.pow(radio,2)) * altura
print(f"El volumen es igual a {volumen:.2f}")



