# Dado 3 numeros enteros verificar cual es mayor

print("Dame 3 numeros separados por un espacio:")
n1 , n2, n3 = input().split()
n1 , n2, n3 = (int(n1), int(n2), int(n3))

if n3 > 1 and n3 > n2:
    print(f"{n3} es el numero mayor")
elif n2 > n1 and n2 > n3:
    print(f"{n2} es el numero mayor")
else:
    print(f"{n1} es el numero mayor")
