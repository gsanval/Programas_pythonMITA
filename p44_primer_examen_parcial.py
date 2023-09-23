# Control de inscripcion de un evento academico
total = 0
while (True):
    print("\nUniversidad Pirata SA de CV")
    print("Sistema de Inscripción Congreso de Sistemas\n")
    print("[1] Alumno $100, [2] Trabajador $200, [3] Docente $500")
    select = int(input("Elige tipo de usuario: \n"))
    print("[1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900")
    select2 = int(input("Elige tipo de paquete: \n"))
    cantidad = int(input("¿Cual es la cantidad?"))

    precio_usuario = 0
    precio_paquete = 0

    if select == 1:
        precio_usuario = 100
    elif select == 2:
        precio_usuario = 200
    elif select == 3:
        precio_usuario = 500
    else:
        print("\nTipo de usuario no valido. Por favor, inténtelo de nuevo.")
        continue

    if select2 == 1:
        precio_paquete = 600
    elif select2 == 2:
        precio_paquete = 800
    elif select2 == 3:
        precio_paquete = 900
    else:
        print("\nTipo de paquete no valido. Por favor, inténtelo de nuevo.")
        continue
    
    subtotal0 = (precio_usuario + precio_paquete) * cantidad
    subtotal = (precio_usuario + precio_paquete) * cantidad
    subtotal2 = (precio_usuario + precio_paquete) * cantidad
    total2 = 0
    if subtotal > 5000:
        if select == 1:
            subtotal = subtotal * 0.80
            subtotal2 = subtotal2 - subtotal
            total2= total2 + subtotal
        elif select == 2:
            subtotal = subtotal * 0.90
            subtotal2 = subtotal2 - subtotal
            total2= total2 + subtotal

        elif select == 3:
            subtotal = subtotal * 0.95
            subtotal2 = subtotal2 - subtotal
            total2= total2 + subtotal
    

    print(f"Tu pedido fue : {cantidad}, Tipo de usario: {select}, Tipo de paquete: {select2}")
    print(f"Subtotal: {subtotal0}, y con un descuento de {subtotal2} dando un total de {total2}")
    total = total + subtotal

    res = input("Deseas continuar(S/N)?").upper()
    if res == "N": break
print(f"Importe total de venta: {total}")
print("\nProceso terminado...")
