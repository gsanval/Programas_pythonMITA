
datos = {}

print("Introduce nombres y edades, * en el nombre para terminar")
while(True):
    nombre = input("Nombre: ")
    if nombre == "*":
        break
    else:
        datos[nombre] = int(input("Edad : "))

print("\nLos datos introducidos son:\n",datos,len(datos))

s = p = 0
for i,j in datos.items():
    print(f"{i:<5} - {j:>3}")
    s = s + j
print(datos)
p = s/len(datos)
print(f"\nLa suma es {s} y el promedio es {p}")
