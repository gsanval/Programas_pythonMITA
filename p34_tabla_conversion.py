# Imprimir una tabla de conversion de peso a dolar

tc = 19.70 ; tcl = 21.22
while(True):

    while (True):
        pi = float(input("Valor inicial: "))
        pf = float(input("Valor final: "))
        if (pi < pf):
            break

    print("Pesos\t Dolar\t Libra")
    print("-"*15)
    c = pi
    while (c<=pf):
        print(f"{c}\t{c/tc:.2f}\t{c/tcl:.4f}")
        c = c + 1
    print("-"*15)
    res = input("Deseas continuar(S/N)?").upper()
    if res == "N": break

print("\n Proceso terminado")
