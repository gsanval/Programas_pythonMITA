# Imprime los pares y los suma.

n = int(input("Dame un numero: "))

s = 0
for par in range(2,n+1,2):
    print(par, end=" ")
    s = s + par
print("\nLa suma de los pares es:", s)