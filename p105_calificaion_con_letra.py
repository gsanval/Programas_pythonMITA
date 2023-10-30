# Regresa una letra y un mensaje de acuerdo al promedio

def caliletra(prom):
    letra = ""
    msj = ""
    if prom>=90 and prom <=100:
        letra = "A"
        msj = "Excelente"
    elif prom>=80 and prom<90:
        letra = "B"
        msj = "Bien"
    elif prom>=70 and prom<80:
        letra = "C"
        msj = "Suficiente"
    elif prom>=60 and prom<70:
        letra = "D"
        msj = "Deficiente"
    elif prom >=50 and prom <60:
        letra = "F"
        msj = "Reprobado"
    return letra, msj

#Programa principal
prom = 91
letra, msj = caliletra(prom)


print(f"Tu prom es de {prom} corresponde a la letra {letra} y es {msj}")
