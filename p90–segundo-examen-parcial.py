# Se desea procesar el pedido de una pizza en base a sus ingredientes.
while(True):
    ingredientes = {
    "T" : 1.50, 
    "P" : 3.50, 
    "A" : 0.40, 
    "Q" : 3.74, 
    "I" : 2.10 
    }
    orden = input("Ingredientes de tu pizza?: \n").upper()
    precioi = 15
    total = precioi
    ingredientes_validos = True
    if len(orden) == 0:
        print("Precio base es de 15, compra de más de 20 descuento del 5%\n")
        print(ingredientes)
    else:
        for i in orden:
            if i in ingredientes:
                total = total + ingredientes[i]
            else:
                print("No seleccionaste ingredientes validos")
                ingredientes_validos = False
                break

        if ingredientes_validos == True:
            if total >= 30:
                des = total * 0.05
                total2 = total - des
                print(f"El subtotal es: {total:.2f}")
                print(f"El total es: {total2:.2f}")

            else:
                print(f"El subtotal es: {total:.2f}")
                print(f"El total es: {total:.2f}")
    res = input("Deseas hacer otra orden (S/N)?:").upper()
    if res == "N": break

print("Gracias por su preferencia")

