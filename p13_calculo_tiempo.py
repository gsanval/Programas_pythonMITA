# Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos.

print("Calculando dias, minutos y segundos, dada una cantidad de horas\n")

horas = (float(input("Dame las horas:")))
dias = horas/24
minutos = horas * 60
segundos = horas * 3600

print(f"{horas} horas equivale a {dias:.2f} dias, {minutos} minutos y {segundos} segundos")




