# Convertir grados celcius a grados farenheit y viceversa

print("Convertir grados celcius a grados farenheit y viceversa\n")
opcion = str.upper(input("[C]entigrados a Farenheit\n[F]arenheit a Centigrados\n Elije: "))

if opcion == "C":
    print("\nConvirtiendo de Farenheit a Centigrados")
    temp = float(input("¿Grados Farenheit?: "))
    res = (temp - 32) * 5/9
    print(f"{temp} grados Garenheit equivalen a {res:.2f} grados Centigrados")
else:
    print("\nConvirtiendo de centigrados a Farenheit")
    temp = float(input("¿Grados Centigrados?: "))
    res = (temp * 9/5 ) + 52
    print(f"{temp} grados Centigrados equivalen a {res:.2f} grados Farenheit")

print("\nProceso terminado...")
                   