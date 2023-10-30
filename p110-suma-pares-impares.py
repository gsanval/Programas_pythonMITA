def suma_pares_o_impares(inicio, fin, opcion):
    suma = 0
    if opcion == 'P':
        suma = sum(num for num in range(inicio, fin + 1) if num % 2 == 0)
    elif opcion == 'I':
        suma = sum(num for num in range(inicio, fin + 1) if num % 2 != 0)
    return suma


print("Menú:")
print("1. Sumar números pares en un rango")
print("2. Sumar números impares en un rango")

opcion_menu = input("Seleccione una opcion (1-2): ")

if opcion_menu in ('1', '2'):
    inicio = int(input("Ingrese el inicio del rango: "))
    fin = int(input("Ingrese el fin del rango: "))
    resultado = suma_pares_o_impares(inicio, fin, 'P' if opcion_menu == '1' else 'I')
    print(f"La suma es: {resultado}")
else:
    print("Opción no valida.")
