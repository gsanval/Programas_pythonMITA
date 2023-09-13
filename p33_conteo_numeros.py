# Cuenta nueros los suma , cuneta positivos, negativos y cero, se detiene al introducir 999

cuenta = suma = cp = cn = cc = 0
while (True):
    num = int(input("Numero?: "))
    if num != 999:
        cuenta = cuenta +1
        suma = suma + num
        if num > 0:
            cp = cp + 1
        elif num < 0:
            cn = cn + 1
        else:
            cc = cc +1
    else:
        break

print(f"Se introdujeron {cuenta} numeros")
print(f"La suma de los numeros es {suma}")
print(f"Los posiyivos son {cp}")
print(f"Los negativos son {cn}")
print(f"Los ceros son {cc}")
