# Pares descendidentes del 100 al que el usuario decida.

while(True):
    c = 100
    y = int(input("Donde desea parar?"))
    s = 0
    while c >= y:
        if c % 2 == 0:
            print(c, end = " ")
            s = s + c
        c = c - 1
        
    print(f"\nLa suma de los numeros pares es: {s}")


    resp = input("\nDeseas continuar(S/N)?\n").upper()
    if resp == "N": break
print("Proceso terminado...") 