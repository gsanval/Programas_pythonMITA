# Calcular suma y promedio de una serie de numeros intriducidos por el teclado hasta introducir 0, cuenta cuantos numeros se introdujeron.

while(True):
    suma = cuenta = 0
    while (True):
        num = int(input("Numero?: "))
        if num != 0:
            cuenta = cuenta + 1
            suma = suma + num
        else:
            break

    prom = suma / cuenta    
    print(f"Cuenta de numeros introducidos: {cuenta}")
    print(f"La suma de los numeros introduciodos: {suma}")
    print(f"El promedio de los numeros introducidos es: {prom}")
    resp = input("\nDeseas continuar(S/N)?\n").upper()
    if resp == "N": break
print("Proceso terminado...")
