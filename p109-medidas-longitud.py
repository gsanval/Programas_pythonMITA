# Convertir de pulgadas a centímetros y metros a pies.

def pulcem(med):
    return med * 2.54

def mepi(med):
    return med * 3.281


# Programa principal 

print("[P]ulgadas a centimetros")
print("[M]etros a pies")

op = input("Elije: ").upper()
if op == "P":
    med = int(input("Dame las pulgadas: "))
    print(f"Los cm son: {pulcem(med)}")
elif op == "M":
    med = int(input("Dame los metros: "))
    print(f"Los pies son: {mepi(med)}")

else:
    print("Opcion incorrecta")
