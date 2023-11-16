
class Jugador:
    def __init__(self, nombre, año, sexo, becado):
        self.nombre = nombre
        self.año = año
        self.sexo = sexo
        self.becado = becado
    def __str__(self):
        return f"Nombre: {self.nombre}, Año: {self.año}, Sexo = {self.sexo}, Becado: {'Becado' if self.becado else 'Sin Beca'}"

class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = list()

    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)

    def calcularSubtotal(self):
        subtotal = 0
        for jugador in self.jugadores:
            if not jugador.becado:
                subtotal = subtotal + self.costo
        return subtotal
    def __str__(self):
        return f">{self.nombre} -- {self.rango} -- {self.costo}"
    
class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = list()

    def agregarCategoria(self, categoria):
        self.categorias.append(categoria)
    def calcularTotales(self):
        totalC = len(self.categorias)
        totalH = 0
        totalM = 0
        total = 0
        for categoria in self.categorias:
            for jugador in categoria.jugadores:
                if jugador.sexo == "Hombre":
                    totalH = totalH + 1
                elif jugador.sexo == "Mujer":
                    totalM = totalM + 1
            total = total + categoria.calcularSubtotal()
        return totalC, totalH, totalM, total
    
def main():
    jugador1 = Jugador("Alexander Lopez", 2006, "Hombre", False)
    jugador2 = Jugador("Uriel Puga", 2007, "Hombre", True)
    jugador3 = Jugador("Alejandra Escalona", 2008, "Mujer", False)
    jugador4 = Jugador("Armando Santana", 2009, "Hombre", False)
    jugador5 = Jugador("Daniel Mijares", 2010, "Hombre", False)
    jugador6 = Jugador("Antonio Hernandez", 2011, "Mujer", True)
    jugador7 = Jugador("Andrea Solis", 2012, "Mujer", True)
    jugador8 = Jugador("Marissa Hernandez", 2013, "Mujer", True)
    jugador9 = Jugador("Diana Soto", 2014, "Mujer", False)

    categoria1 = Categoria("Junior A", "2006/2007/2008", 1250.00)
    categoria1.agregarJugador(jugador1)
    categoria1.agregarJugador(jugador2)
    categoria1.agregarJugador(jugador3)
    categoria2 = Categoria("Junior B", "2009/2010/2011", 850.00)
    categoria2.agregarJugador(jugador4)
    categoria2.agregarJugador(jugador5)
    categoria2.agregarJugador(jugador6)
    categoria3 = Categoria("Pony A", "2012/2013/2014", 700.00)
    categoria3.agregarJugador(jugador7)
    categoria3.agregarJugador(jugador8)
    categoria3.agregarJugador(jugador9)

    academia = Academia("Academia America Club de Futbol", "Gerardo Sánchez Sandoval", "Aguanaval 123 Hidráulica")
    academia.agregarCategoria(categoria1)
    academia.agregarCategoria(categoria2)
    academia.agregarCategoria(categoria3)
    totalC, totalH, totalM, total = academia.calcularTotales()

    #Reporte:
    print("\nReporte de Club Deportivo:\n")
    print(f"Nombre: {academia.nombre}")
    print(f"Propietario: {academia.propietario}")
    print(f"Domicilio: {academia.domicilio}\n")
    print(f"Total de categorias: {totalC}")
    print(f"Total de Hombres: {totalH}")
    print(f"Total de Mujeres: {totalM}\n")
    print(">> Datos generales de las categorias:\n")
    for categoria in academia.categorias:
        print(f"{categoria}")
    print("\n>> Jugadores por categoria:")
    for categoria in academia.categorias:
        print(f"\n{categoria} -- ({len(categoria.jugadores)})\n")
        for jugador in categoria.jugadores:
            print(f"{jugador}")
        subtotal = categoria.calcularSubtotal()
        print(f"- Subtotal: {subtotal:.2f}")
    print(f"-> Total: {total:.2f}")
    
if __name__ == "__main__":
    main()
