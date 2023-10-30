# Determina el menor de tres numeros

def menor(n1,n2,n3):
    men = 0
    if n1<n2 and n1<n3:
        men = n1
    elif n2<n1 and n2<n3:
        men = n2
    else:
        men = n3
    return men

# Programa principal
print("Dame 3 numeros: ")
n1,n2,n3 = float(input()), float(input()), float(input())

men = menor(n1,n2,n3)
print(f"El menor  de los tres numeros es {men}")
