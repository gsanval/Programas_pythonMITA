# Uso de funciones trigonometricas en python
import math

print("Calculo de las funciones trigonometricas basicas\n")

angulo = float(input("Dame un angulo en grados:"))
angrad = math.radians(angulo)

seno = math.sin(angrad)
coseno = math.cos(angrad)
tangente = math.tan(angrad)

#print(f"Seno: {seno}\n Coseno: {coseno}\n Tangente: {tangente}")

salida = ("Resumen de funciones\n"
f"EL seno es: {seno}\n"            
f"EL coseno es: {coseno}\n"            
f"La tangente es: {tangente}\n"
f"El angulo de {angulo} grados, equivale a: {angrad}radianes"
)
print(salida)            