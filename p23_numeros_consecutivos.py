# Verificar si los numeros son consectivos

print("Dame 3 numeros consecutivos separados por un espacio:")
n1 , n2, n3 = input().split()
n1 , n2, n3 = (int(n1), int(n2), int(n3))

if n2 - n1 == 1 and n3 - n2 == 1:
    print("Los numeros son consecutivos")
else:
    print("Los numeros no son consecutivos")


