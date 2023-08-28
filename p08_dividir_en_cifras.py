# Dividir un numero de 3 cifras en centenas, decenas y unidades

numero = int(input("Dame un numero con tres cifras: "))

centenas = numero //100
decenas = (numero - centenas * 100) //10
unidades = numero - (centenas * 100 + decenas *10)

print(f"Centenas: {centenas}\n Decenas: {decenas}\n Unidades: {unidades}")
print(f"Suma de digitos: {centenas+decenas+unidades}")
