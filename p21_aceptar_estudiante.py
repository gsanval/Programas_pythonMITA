# Aceptar a un estudiante en base a la edad y sus califiaciones

nombre = input("Dame tu nombre : ")
edad = int(input("Dame tu edad : "))

if edad >= 18:
    print("Continuamos...")
    print("Dame 2 calificaciones separadas por enter:")
    c1, c2 = int(input()), int(input())
    if c1 >=8 and c2>=8:
        print(f"{nombre} bienvenido tus calificaciones son {c1} y {c2}")
    else:
        print("Solo aceptamos calificaiones maayores a 8")

else:
    print("Solo aceptamos mayores de 18")

print("\nProceso terminado...")


