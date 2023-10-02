#Imprime la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma.

n = int(input("Dame el numero que deseas: "))
suma = 0
for h in range(1,n+1):
    print(f"1/{h} + ", end="")
    arm = 1/h
    suma = suma + arm
print(f"\nSuma: {suma}")
