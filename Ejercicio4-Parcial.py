class Vehiculo:
    def __init__(self, tipo, modelo, coste_renta):
        self.tipo = tipo
        self.modelo = modelo
        self.coste_renta = coste_renta
        self.disponible = True  # Por defecto, el vehículo está disponible

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos_rentados = []

class EmpresaRentaVehiculos:
    def __init__(self):
        self.vehiculos = []
        self.registro_rentas = {}

    def registrar_vehiculo(self, tipo, modelo, coste_renta):
        nuevo_vehiculo = Vehiculo(tipo, modelo, coste_renta)
        self.vehiculos.append(nuevo_vehiculo)
        print(f"Vehículo registrado: {tipo} {modelo} con coste de renta de ${coste_renta} por día.")

    def mostrar_vehiculos_disponibles(self):
        print("Vehículos disponibles para renta:")
        for vehiculo in self.vehiculos:
            if Vehiculo.disponible:
                print(f"- {Vehiculo.tipo} {Vehiculo.modelo}, Coste de renta: ${Vehiculo.coste_renta} por día")

    def rentar_vehiculo(self, cliente, tipo, modelo):
        for vehiculo in self.vehiculos:
            if Vehiculo.tipo == tipo and Vehiculo.modelo == modelo and Vehiculo.disponible:
                Vehiculo.disponible = False
                Cliente.vehiculos_rentados.append(vehiculo)
                self.registro_rentas[cliente] = vehiculo
                print(f"Vehículo {tipo} {modelo} rentado a {Cliente.nombre} con éxito.")
                return
        print(f"No hay {tipo} {modelo} disponible para renta en este momento.")