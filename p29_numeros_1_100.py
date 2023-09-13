# Imprimir numeros del 1 al 100 de uno en uno

x = int(input("Hasta donde deseas llegar?"))
p = int(input("De cuanto en cuanto?"))

n = 1
while n <= x:
    print(n, end= " ")
    n = n + p
