# Calcular el facorial

def factorial(n):
    f = 1
    for n in range(1,n+1):
        f = f*n
    return f


# Programa principal
n = int(input("Numero ?"))
print(f"El facorial de {n} es {factorial(n)}")