# Imprimir tabla de multiplicar que el usario desee usando un ciclo for

while(True):
    t = int(input("Que tabla deseas? "))
    n = int(input("Hasta donde quieres la tabla? "))

    for i in range(1,n+1):
        print(f"{t}x{i}={t*i}")
    res = input("Deseas continuar (S/N)?:").upper()
    if res == "N": break

print("Proceso terminado...")
