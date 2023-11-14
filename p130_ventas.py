class Venta:
    def __init__(self, articulo, cantidad, precio):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = precio
        self.total = cantidad*precio
    def __str__(self):
        return f"Articulo: {self.articulo:<15}, Cantidad: {self.cantidad:>10.2f}, Precio: {self.precio:>10,.2f}, Total: {self.total:>10,.2f}"
    
class Cliente:
    def __init__(self, rfc, nombre, domicilio, correo):
        self.rfc = rfc
        self.nombre = nombre
        self.domicilio = domicilio
        self.correo = correo
        self.ventas = list()
    def agregarVenta(self, venta):
        self.ventas.append(venta)
    def totalImporteVentas(self):
        total = 0
        for venta in self.ventas:
            total = total + venta.total
        return total
    def __str__(self):
        return f"Cliente --> [Nombre: {self.nombre:<15}, RFC: {self.rfc:<12}, Domicilio: {self.domicilio:<20}, Correo: {self.correo:<20}]"
    

class Tienda:
    def __init__(self, nombre, domicilio, propietario):
        self.nombre = nombre
        self.domicilio = domicilio
        self.propietario = propietario
        self.clientes = list()
    def agregarCliente(self, cliente):
        self.clientes.append(cliente)
    def totalVentas(self):
        total = 0
        for cliente in self.clientes:
            total = total + len(cliente.ventas)
        return total
    def totalImporteVentas(self):
        total = 0
        for cliente in self.clientes:
            total = total + cliente.totalImporteVentas()
        return total
    def __str__(self):
        return f"Tienda --> [Nombre: {self.nombre}, Domicilio: {self.domicilio}, Propetiario: {self.propietario}]"
    
def main():
    print("Inicio del programa principal en la funcion main()\n")
    mitienda = Tienda(nombre="Ferreteria las Lomas", domicilio="Av. Luis Moya #225", propietario="Gerardo Sánchez")
    mitienda.agregarCliente(Cliente(rfc="JELI20240", nombre= "Felipe Calderon", domicilio="Las Lomas #223", correo="asd@gmail.com"))
    mitienda.agregarCliente(Cliente(rfc="PEÑA12105", nombre= "Enrique Peña", domicilio="5 de Mayo #789", correo="enriqu89@gmail.com"))
    mitienda.agregarCliente(Cliente(rfc="ALMO01202", nombre= "Andres Lopez", domicilio="Palacio Nacional #098", correo="amlo123@gmail.com"))
    mitienda.agregarCliente(Cliente(rfc="GELA09190", nombre= "Xochitl Gelatinas", domicilio="Doneon #666", correo="xochitl@gmail.com"))
    mitienda.clientes[0].agregarVenta(Venta(articulo="Martillo", cantidad= 10, precio=60.5))
    mitienda.clientes[0].agregarVenta(Venta(articulo="Pala", cantidad= 2, precio=1170.55))
    mitienda.clientes[1].agregarVenta(Venta(articulo="Clavo", cantidad= 2.5, precio=160.34))
    mitienda.clientes[1].agregarVenta(Venta(articulo="Cinta de aislar", cantidad= 5, precio=71.34))
    mitienda.clientes[2].agregarVenta(Venta(articulo="Tiner", cantidad= 50, precio=65))
    mitienda.clientes[3].agregarVenta(Venta(articulo="Pinzas", cantidad= 1, precio=800))

    #Reporte
    print(f"Reporte de ventas: {mitienda}")
    print(f"Total clientes: ", len(mitienda.clientes))
    print(f"Total ventas: {mitienda.totalVentas()}")
    print("\nClientes")
    for cliente in mitienda.clientes:
        print(cliente)
    for cliente in mitienda.clientes:
        print(f"\n{cliente.rfc} - {cliente.nombre} - {cliente.totalImporteVentas():,.2f}")
        for venta in cliente.ventas:
            print(f"- {venta}")
    print(f"Total importe ventas: {mitienda.totalImporteVentas():,.2f}")
if __name__ == "__main__":
    main()
