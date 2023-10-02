# Imprime el factorial de un numero

n = int(input("Dame el numero que deseas el factorial: "))
f = 1
for h in range(1,n+1):
    print(h, end="*")
    f = f * h

print("=",f)