# Funcion que al ser invocada usa el nombre del parametro

def saluda(apaterno, amaterno, nombre):
    print(f"Hola {apaterno}, {amaterno}, {nombre}")

saluda("Sanchez", "Sandoval", "Gerardo")
saluda(nombre="Carlos",apaterno="Sanchez",amaterno="Sandoval")
