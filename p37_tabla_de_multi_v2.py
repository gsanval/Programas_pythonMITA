# Imprime la tabla del 1 hatsa n 

n  = int(input("Hasta que tabla vas a querer? "))
m = int(input("Hasta donde?: "))
t = 1
while(True):
    while (t <=n):
        print(f"\n Tabla del {t}\n")
        c = 1
        while c<=m:
            print(f"{t} x {c} = {t*c}")
            c = c +1
        t = t + 1
    resp = input("Deseas continuar(S/N)?").upper()
    if resp == "N": break

print("\nProceso terminado")
