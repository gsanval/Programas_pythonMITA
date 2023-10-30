# Imprime un cuadro de r x c de un caracter det

def cuadro(r, c, car):
    for i in range(1,r+1):
        for j in range(1,c+1):
            print(car, end=" ")
        print()

# Programa principal 
r = int(input("Renglones ?"))
c = int(input("Columnas ?"))
car = int(input("Caracter ?"))
cuadro(r,c,car)



cuadro(3,8,"@")