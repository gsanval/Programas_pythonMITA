# muestra el tipo de angulo 
# <90 agudo, = 90 recto y <180 obtuso, =180 llano y <360 concavo, = 360 completo

angulo = int(input("Dame el angulo: "))

if angulo>=0 and angulo<=360:
    print("Continuar...")
    if angulo < 90:
        print("agudo")
    elif angulo == 90:
        print("recto")
    elif angulo>= 90 and angulo<180:
        print("Obtuso")
    elif angulo == 180:
        print("llano")
    elif angulo>180 and angulo<360:
        print("concavo")
    else:
        print("completo")
else:
    print("Esta fuera de rango")

