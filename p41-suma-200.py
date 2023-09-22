# Calculcar la suma de numeros introduciodos por el usuario hasta que la suma sea >= 200, mostrar suma y cuantos numeros fueron introduciodos.

while(True):
    suma = cuenta = 0
    while (True):
        num = int(input("Numero?: "))
        cuenta = cuenta + 1
        suma = suma + num
        if suma >= 200: break
    
    print(f"La cuenta de los numeros introducidos es: {cuenta}")
    print(f"La suma de los numeros introoducidos es: {suma}")
    resp = input("\nDeseas continuar(S/N)?\n").upper()
    if resp == "N": break
print("Proceso terminado...")
