# Se van a procesar dos diccionarios

nombres = {"Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"}
sueldos = {4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00}

nomsu = dict(zip(nombres,sueldos))
print("Diccionario con nombres y sueldos:\n",nomsu)

print("\nLas llaves:")
for i in nomsu.keys():
    print(i, end= " ")

print("\nLos valores")
for v in nomsu.values():
    print(v, end=" ")

print("\nLas llaves y valores a la vez:")
s = 0
for i,v in nomsu.items():
    print(f"{i:<10} : {v}")
    s = s + v

p = s / len(nomsu)
print(f"La suma es {s:.2f} y el promedio es: {p:.2f}")