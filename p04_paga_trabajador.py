# Calcula la paga de un trabajador

print("Calculando la paga total de un trabajador\n")

nombre = input("Dame tu nombre: ")
horas = int(input("Horas trabajadas: "))
paga = float(input("Paga por hora: "))

tasa = 0.03

pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print("\nResumen de pagos:\n")
print(f"{nombre} trabajo {horas} horas con una paga de {paga} pesos a una tasa de {tasa}")
print(f"Paga bruta:   {pagabruta}")
print(f"Impuesto:   {impuesto}")
print(f"Paga neta:   {paganeta}")
