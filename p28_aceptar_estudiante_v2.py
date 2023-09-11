# Aceptar a un estudiante en base a la edad y sus califiaciones

nombre = input("Dame tu nombre : ")
edad = int(input("Dame tu edad : "))
sexo = int(input("Dame tu sexo (1 para hombre, 2 para mujer): "))

if edad >= 21 and sexo == 2:
    print("Continuamos...")
    print("Dame 3 calificaciones separadas por enter:")
    c1, c2, c3 = int(input()), int(input()), int(input())
    prom = (c1+c2+c3)/3
    if 8 <= prom <= 9.5: 
        print(f"{nombre} bienvenido a la Universidad Kitty Kat SA, tu promedio {prom}, edad {edad} y genero son adeucados.")
    else:
        print("Tus calificaciones no cumplen con el promedio requerido")

else:
    print("Solo aceptamos mayores a 21 y mujeres")

print("\nProceso terminado...")