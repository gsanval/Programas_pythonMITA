# Funcion con varios parametros

def saluda(nombre,edad,telefono,correo):
    print("*"*120)
    print(f"Bienvenido {nombre} tu edad es {edad}, tu telefono es {telefono}, tu correo es {correo}.", end=" ")
    if (edad>=18): print("Eres mayor de edad.")
    else: print("Eres menor de edad")

saluda("Gerardo Sanchez", 22, "4922240584", "gsanval@gmail.com")