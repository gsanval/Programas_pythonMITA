# Conjetura de collatz


while(True):
    while(True):
        num = int(input("Dame un numero positivo"))
        if num > 0: break

    while (num !=1):
        print(num, end = " ")
        if num % 2 == 0 :
            num = num / 2
        else:
            num = num * 3 + 1
    print(num, end = " ")

    res = input("Deseas continuar(S/N)?").upper()
    if res == "N": break

print("\nEl proceso ha acabado...")
