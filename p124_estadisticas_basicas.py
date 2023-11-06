import p118_funciones as p18
import math

def varianza(lista):  
    media = sum(lista) / len(lista)
    varianza = sum((x - media) ** 2 for x in lista) / (len(lista) - 1)
    return varianza

#PP
lista = p18.leer()
print("Lista de numeros: ",lista)
men = p18.menor(lista)
may = p18.mayor(lista)
prom = p18.prmedio(lista)
print("El menor es: ", men)
print("El mayor es: ", may)
print(f"La media es: {prom:.2f}")
var = varianza(lista)
print(f"La varianza es: {var:.2f}")
print(f"La desviacion estrandar es: {math.sqrt(var)}")

