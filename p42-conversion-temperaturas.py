# Convertir grados centigrados a farenheit de un valor inicial a un final en intervalos de 1 a 1.
while(True):
    while(True):
        ti = float(input("Dame una temperatura inicial en grados centigrados: "))
        tf = float(input("Dame una temperatura final en grados centigrados: "))
        if ti < tf:
            break
    print("Grados(C)\tGrados(F)\t")
    print("-"*30)
    c = ti
    while(c<=tf):
        print(f"{c}\t          {c*(9/5)+32}\t")
        c = c + 1
    print("-"*30)
    res = input("Deseas continuar(S/N)?").upper()
    if res == "N": break

print("\n Proceso terminado")



