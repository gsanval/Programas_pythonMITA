# EStudiante 

estudiante = { 
    "nombre" : "Juan Perez",
    "edad" : 45,
    "correo" : "jperez@gmail.com",
    "carrera" : "Sistemas"
}
print(f"\nDiccionario original: \n {estudiante}")
estudiante["calificacion"] = 9.5
estudiante["correo"] = "juanp@hotmail.com"
print(f"\nDiccionoario actualizado: \n {estudiante}")

print("\nLas llaves:")
for i in estudiante.keys():
    print(i, end= " ")

print("\nLos valores")
for v in estudiante.values():
    print(v, end=" ")

print("\nLas llaves y valores a la vez:")
for i,v in estudiante.items():
    print(f"{i:<10} : {v}")