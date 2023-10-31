# Calcular el promedio de una lista de numeros

def leer():
    lista = []
    while (True):
        n = float(input("Numero: "))
        if n ==-1: break
        lista.append(n)
    return lista

def prmedio(lista):
    s = 0
    for n in lista:
        s = s + n
    return s / len(lista)

def mayoeprom(lista,prom):
    mp = []
    for n in lista:
        if n > prom:
            mp.append(n)
    return mp

# PP
lista = leer()
print(lista, len(lista))
prom = prmedio(lista)
print("El promedio es", prom)
mp = mayoeprom(lista,prom)
print("Los numeros mayores al promedio son", mp, len(mp))
