# Calcular el promedio de 3 calificaiones

print("Calcular el promedio de las tres calificaciones\n")
print("Dame 3 calificaciones:")
c1, c2, c3 = input().split()
c1, c2, c3 = [float(c1), float(c2), float(c3)]

prom = (c1+c2+c3)/3
print(f"Las calificaciones son {c1},{c2},{c3} y el promedio es {prom}")

