# Imprimir las tablas del 1 a n, de 1 hasta m

while(True):
    n = int(input("Hasta que tabla quieres? "))
    m = int(input("Hasta donde? "))

    for i in range(1,n+1):
        print(f"\nTabla del {i}\n")
        for j in range(1,m+1):
            print(f"{i}x{j}={i*j}")
    res = input("Deseas continuar (S/N)?:").upper()
    if res == "N": break

print("Proceso terminado...")
