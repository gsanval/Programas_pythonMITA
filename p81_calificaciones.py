
materias = [
    "Fisica","Quimica","Matematicas","Geografia","Estadistica"
]

califs = [10,9,8,7.5,6]
print("Lista de materias", materias)
print("Lista de calificaciones", califs)

notas = dict(zip(materias,califs))
print("\nLas notas: ",notas,len(notas))

notas.update({"ingles":10})
notas.update({"programacion":7})
print("\nDiccionario actualizado: ",notas,len(notas))
notas.pop("Fisica")
notas.popitem()
print("\nDiccionario actualizado: ",notas,len(notas))
notas.update({"Quimica":10})
notas.update({"Matematicas":10})
# otra forma
# notas["Quimica"] = 10
# notas["Matematicas"] = 10
print("\nDiccionario actualizado: ",notas,len(notas))
s = p = 0
for m,c in notas.items():
    print(f"{m:<12} - {c:>5.2f}")
    s = s + c
p = s / len(notas)
print(f"La suma es {s} y el promedio es: {p}")
