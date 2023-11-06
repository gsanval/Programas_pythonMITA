
def leer():
    lista = []
    while (True):
        n = int(input("Numero: "))
        if n ==-1: break
        lista.append(n)
    return lista

def sumdigitos(n):
    suma = 0
    while n!=0:
        dig = n % 10
        suma = suma + dig
        n = n//10
    return suma

def suma_digitos_lista(lista):
    sumas = []
    for numero in lista:
        suma = sumdigitos(numero)
        sumas.append(suma)
    return sumas

lista = leer()
print("La lista de los numeros es: ", lista)
res = suma_digitos_lista(lista)
print("La suma de los digitos es: ", res)