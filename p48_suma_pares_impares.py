# Imprime los pares y su suma, los impares y su suma, en el rango de 1 a n


while(True):
    n = int(input("Hasta donde deseas pares e impares?: "))

    s = 0
    print("Imprimir numeros pares y su suma")
    for par in range(2,n+1,2):
        print(par, end=" ")
        s = s + par
    print("\nLa suma de los pares es:", s)

    s = 0
    print("Imprimir los numeros impares y su suma")
    for impar in range(1,n+1,2):
        print(impar, end=" ")
        s = s + impar
    print("\nLa suma de los numeros impares es,", s)
    res = input("Deseas continuar (S/N)?:").upper()
    if res == "N": break

print("Proceso terminado...")