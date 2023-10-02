
x = int(input("Desde donde comenzar a descender? "))
y = int(input("De cuanto en cuanto se desciende? "))

for n in range(x,0,-y):
    print(n, end= " ")
