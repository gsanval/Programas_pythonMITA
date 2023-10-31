# Calcula la suma de una lista de numeros usando una funcion 

def suma(lista):
    s = 0
    for n in lista:
        s = s + n
    return s 

# Programa principal 
lista = []
while (True):
    n = float(input("Numero: "))
    if n ==-1: break
    lista.append(n)
print(lista,len(lista))
res = suma(lista)
print("La suma es", res)