# Creamos un modulo de funciones

def suma(lista):
    s = 0
    for n in lista:
        s = s + n
    return s 

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

def prmedio(lista):
    s = 0
    for n in lista:
        s = s + n
    return s / len(lista)

def leer():
    lista = []
    while (True):
        n = float(input("Numero: "))
        if n ==-1: break
        lista.append(n)
    return lista