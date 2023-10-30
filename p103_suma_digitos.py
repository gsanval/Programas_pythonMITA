# Suma los digitos de un numero entero 1971 = 18

def sumdigitos(n):
    suma = 0
    while n!=0:
        dig = n % 10
        suma = suma + dig
        n = n//10
    return suma
    
print(sumdigitos(123))

# Progrma principal

año = int(input("Dame tu año y te doy tu numero de la suerte: "))
suerte = sumdigitos(año)
print(f"Tu año de nacimiento es {año} y tu numero es {sumdigitos(año)}")