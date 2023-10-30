# Funcion que recibe un numero arbitrario de parametros

def saludos(*todos):
    print("Saludos a: ", todos)
    for nomre in todos:
        print("Hola, ",nomre)
    if len(todos) != 0:
        print("El primero es el primero y es", todos[0])
        print("El ultimo es el ultimo y es", todos[-1])



saludos("Jose", "Juan", "Pedro", "Luis", "Rocio", "Matias", "Alfredo", "Mercedes")
