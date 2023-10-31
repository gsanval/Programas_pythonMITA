# Calcula el mayor y menor de una lista de numeros usando funciones

def leer():
    lista = []
    while (True):
        n = float(input("Numero: "))
        if n ==-1: break
        lista.append(n)
    return lista

def menor(lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

#Programa principal
lista = leer()
print(lista, len(lista))
men = menor(lista)
may = mayor(lista)
print("El menor es", men)
print("El mayor es", may)
