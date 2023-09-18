# Imprime tablas de multiplicar


while(True):


    t = int(input("Caul tabla?: "))
    n = int(input("Hasta donde?: "))
    c = 1
    while c <=n :
        print(f"{t} x {c} = {t*c}")
        c = c + 1
    res = input("Deseas continuar(S/N)?").upper()
    if res == "N": break

print("\nProceso terminado")