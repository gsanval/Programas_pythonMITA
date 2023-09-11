# Programa que convierte una cifra del 1 al 10 en numero romano

op = int(input("Dame un numero del 1 al 10: "))
if op < 0 or op > 10:
    print("Fuera de rango")
else:
    if op == 1:
        print("I")
    elif op == 2:
        print("II")
    elif op == 3:
        print("III")
    elif op == 4:
        print("IV")
    elif op == 5:
        print("V")
    elif op == 6:
        print("VI")
    elif op == 7:
        print("VII")
    elif op == 8:
        print("VIII")
    elif op == 9:
        print("IX")
    else:
        print("X")