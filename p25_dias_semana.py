#Dado un numero entre 1 a 7 se dara un ida de la semana 

op = int(input("Elige:"))
if op < 0 or op > 7:
    print("error")
else:
    if op == 1:
        print("Domingo")
    elif op == 2:
        print("Lunes")
    elif op == 3:
        print("Martes")
    elif op == 4:
        print("Miercoles")
    elif op == 5:
        print("Jueves")
    elif op == 6:
        print("Viernes")
    else:
        print("Sabado")

