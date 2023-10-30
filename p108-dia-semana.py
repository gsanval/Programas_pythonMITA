# Regresa dia de la semana de un numero del 1 al 7

def semana(n):
    sem = ""
    if n>=1 and n<=7:
        if n == 1:
            sem = "Lunes"
        elif n == 2:
            sem = "Martes"
        elif n == 3:
            sem = "Miercoles"
        elif n ==4:
            sem = "Jueves"
        elif n ==5:
            sem = "Viernes"
        elif n ==6:
            sem = "Sabado"
        elif n ==7:
            sem = "Domingo"
        else:
            sem = "Error"
        return sem


n = int(input("Dame la semana (1-7)?"))
print(f"El dia de la semana es: {semana(n)}")
