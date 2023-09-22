# Calcula el numero mayor de los numeros introduciodos

while(True):
    numero_mayor = 0
    while (True):
        num = input("Numero?: ")
        if num > numero_mayor:
            numero_mayor = num
                     
        if num != 0:
            continue    
        else:
            break
   
    res = input("Deseas continuar(S/N)?").upper()
    if res == "N": break
print("\n Proceso terminado")