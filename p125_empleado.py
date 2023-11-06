
class Empleado:
    def __init__(self, nombre, edad, sexo, casado):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.casado = casado
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {'Mujer' if self.sexo == 'M' else 'Hombre'}, Casado: {'Casado' if self.casado else 'No casado'}"
    
# PP
empl = Empleado("Jose Diaz", 35, "H", True) 
#print("Nombre: ", empl.nombre)
#print("Edad: ", empl.edad)
#print("Sexo: ", empl.sexo)
#print("Casado: ", empl.casado)
print(empl)

emp2 = Empleado("Maria Lopez", 22, "M", False)
print(emp2)

emp3 = Empleado("Rosario Valenzuela", 15, "M", True)
print(emp3)

emp4 = Empleado("Juan Perez", 20, "H", False)
print(emp4)

prom = (empl.edad + emp2.edad + emp3.edad+ emp4.edad)/4
print("Promedio de edades de los empleados", prom)

print(f"Los nombres son: {empl.nombre}, {emp2.nombre}, {emp3.nombre}, {emp4.nombre}")

if (not emp2.casado and not emp4.casado): 
    print(f"{emp2.nombre} se puede casar {emp4.nombre}")

if (empl.casado and emp3.casado):
    print(f"{empl.nombre} no se puede casar con {emp3.nombre} porque ambos estan casados")


