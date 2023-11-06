
def leer():
    lista = []
    while (True):
        n = int(input("Numero: "))
        if n ==-1: break
        lista.append(n)
    return lista

def factorial(n):
    f = 1
    for n in range(1,n+1):
        f = f*n
    return f

def factorial_lista(lista):
    fact = []
    for numero in lista:
        fac = factorial(numero)
        fact.append(fac)
    return fact

lista = leer()
print("La lista de los numeros es: ", lista)
res = factorial_lista(lista)
print("La lista y sus facoriales son: ", res)
