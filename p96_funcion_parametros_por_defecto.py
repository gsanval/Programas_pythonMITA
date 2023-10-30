# Funcion con parametros con valores por defecto o valores pre establecidos

def saludo(nombre="Juan", edad=18):
    print(f"Hola {nombre} tu edad es {edad}")

saludo()
saludo("Rocio")
saludo("Gerardo", 22)
