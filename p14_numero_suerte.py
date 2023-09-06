#Obteniendo numero de la suerte

año = float(input("Dame año de nacimiento: "))
millares = año // 1000
centenas = (año - millares * 1000) //100
decenas = (año - (millares * 1000 +  centenas * 100)) //10
unidades = año - (millares * 1000 + centenas * 100 + decenas *10)

print(f"Digito1 {millares}, \nDigito2: {centenas}\nDigito3: {decenas}\nDigito4: {unidades}")
print(f"Numero de la suerte: {millares+centenas+decenas+unidades}")
