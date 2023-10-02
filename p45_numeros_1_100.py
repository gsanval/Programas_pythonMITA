# Imprime los numeros del 1 al x

x = int(input("Hasta donde llega el ciclo? "))
y = int(input("De cuanto en cuanto? "))

for n in range(1, x+1, y):
    print(n, end= " ")
