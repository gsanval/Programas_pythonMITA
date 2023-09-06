# Calcula la segunda ley de newton

print("[F]uerza f = m * a")
print("[M]asa m = f / a")
print("[A]celeracion a = f / m")
op = input("Elige:").upper()

if op == "F":
    print("\nCalculando la fuerza")
    m = float(input("Dame la masa: "))
    a = float(input("Dame la aceleracion: "))
    f = m * a
    print(f"La fuerza es {f:.2f}")
elif op == "M":
    print("\nCalculando la masa")
    f = float(input("Dame la fuerza: "))
    a = float(input("Dame la aceleracion: "))
    m = f / a
    print(f"La masa es {f:.2f}")
elif op == "A":
    print("\nCalculando la aceleracion")
    f = float(input("Dame la fuerza: "))
    m = float(input("Dame la masa: "))
    a = f / m
    print(f"La alceleracion es {f:.2f}")    
else:
    print("\nOpcion invalida")

print("Proceso terminado")

