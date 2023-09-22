# Imprimir los numeros impares hasta que el usuario decida 

while(True):
    x = int(input("Hasta que numero de impares quieres imprimir? "))
    c = 0
    s = 0
    while c <= x:
        if c % 2 != 0:
            print(c, end = " ")
            s = s + c
        c = c + 1
        
    print(f"\nLa suma de los numeros impares es: {s}")


    resp = input("\nDeseas continuar(S/N)?\n").upper()
    if resp == "N": break
print("Proceso terminado...")


    