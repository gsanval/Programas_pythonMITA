# Imprime una secuencia de números mostrados el numero de renglones que el usuario desee.
n = int(input("Dame un numero: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()