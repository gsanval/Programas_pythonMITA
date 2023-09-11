# calcular el promedio de 5 calificaciones introducidas por el usuario, luego evaluar el resultado e imprimir
# un mensaje de acuerdo al promedio obtenido.
print("Dame 5 califiaciones separadas por un enter: ")
c1, c2, c3, c4, c5 = int(input()), int(input()), int(input()), int(input()), int(input())
prom = (c1+c2+c3+c4+c5)/5

if 0 <= prom <=6:
    print("Estas reprobado")
elif 6 < prom <= 7:
    print("Pasas de panzaso")
elif 7 < prom <= 8:
    print("Muy bien pudes mejorar")
elif 8 < prom <=9:
    print("Exclente sigue asi")
else:
    print("Perfecto tu esfuerzo valio la pena")
