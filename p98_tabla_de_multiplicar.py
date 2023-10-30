# Imrpime la tabla de multiplicar que el usario pida hasta donde la pida

def tab(t,n):
    print(f"Tabla del {t} hasta el {n}")
    for i in range(1,n+1):
        print(f"{t}x{i} = {t*i}")
    print()

t = int(input("Que tabla quieres? :"))
n = int(input("Hasta donde?: "))
tab(t,n)

tab(5,4)
tab(6,4)