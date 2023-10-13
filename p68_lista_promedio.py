
datos = []

print("Introduce los numeros que quieras, * para terminar")


while(True):
    numero = input("Numero: ")
    if numero == "*":
        break
    else:
        numero = float(numero)
        datos.append(numero)

print(datos)
s=0
for i in datos:
    s = s + i

prom = s/len(datos)

print(f"La suma es igual a {s} y el promedio es igual a {prom:.2f}")
