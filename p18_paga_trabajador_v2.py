# Calcular la paga de un trabajador, las horas extras se pagan doble

print("Calcula la paga de un trabajador, las horas extra sse pagan doble\n")

nombre = input("Nombre:")
horas = int(input("Horas trabajadas: "))
paga = float(input("Paga * hora: "))

extra = 0
if horas >40:
    extra = horas -40
    total = (40*paga) + (2*paga)
else:
    total = horas * paga

print(f"{nombre} trabajo {horas} con paga de {paga}, horas extra {extra}, dando un total de {total:.2f}")

