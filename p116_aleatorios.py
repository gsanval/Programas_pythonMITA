# SE genaran dos listas de numeros aleatorios
import random
MAX = 20

def genaraAlea():
    l = []
    for n in range(MAX):
        l.append(random.randint(1,100))
    return l

def sumalistas(l1,l2):
    s = []
    for n in range(MAX):
        s.append(l1[n]+l2[n])
    return s

#PP
l1 = genaraAlea()
print("Lista 1", l1, len(l1))
l2 = genaraAlea()
print("Lista 2", l2, len(l2))
s = sumalistas(l1,l2)
print("La suma de las listas es", s, len(s))

