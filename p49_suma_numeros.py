# Imprime la suma y el promedio de n numeros introducidos por el usuario

n = int(input("Cuantos numeros deseas procesar?: "))

suma = 0
prom = 0
for c in range(1,n+1):
    num = int(input(f"{c}-Numero: "))
    suma = suma + num
prom = suma / n
print("\nLa suma es,",suma)
print("\nEl promedio es,", prom)
