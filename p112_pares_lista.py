def pares(lista):
    p = []
    for n in lista:
        if n%2 ==0:
            p.append(n)
    return p

def leer():
    lista = []
    while (True):
        n = float(input("Numero: "))
        if n ==-1: break
        lista.append(n)
    return lista


#Programa principal
lista = leer()
print(lista, len(lista))
res = pares(lista)
print("La lista con los pares es", res, len(res))