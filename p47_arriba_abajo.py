# Imprimir los numeros de 1 a n o de n a 1 segun el usuario descida

import os

while(True):
    os.system("clear")

    print("[1] Imprimir los numeros del 1 a n")
    print("[2] Imprimir los numeros del n a 1")
    op = int(input("Elige: "))

    if op ==1:
        print("Imprimiendo de 1 a n\n")
        n = int(input("Dame el valor de n: "))
        for z in range(1,n+1,1):
            print(z, end=" ")
    elif op ==2:
        print("Imprimiendo de n a 1\n")
        n = int(input("Dame el valor de n: "))
        for w in range(n,0, -1):
            print(w, end=" ")

    else:
        print("error")
    
    res = input("Deseas continuar (S/N)?:").upper()
    if res == "N": break

print("Proceso terminado...")
