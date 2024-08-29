class Hotel:
    def __init__(self):
        #Aqui un diccionario que almacena los tipos de habitaciones disponibles y sus precios por noche.
        self.habitaciones = {
            "simple": 100,
            "doble": 150,
            "suite": 250
        }
       
        # otro diccionario que almacena los servicios extra disponibles y sus costos
        self.servicios_extra = {
            "piscina": 20,
            "cancha de Golf": 50
        }
       
        # Lista para almacenar las facturas generadas para los clientes
        self.facturas = []

    def mostrar_habitaciones(self):
        # Muestra los tipos de habitaciones que tenemos disponibles y sus precios
        print("Habitaciones disponibles:")
        for tipo, precio in self.habitaciones.items():
            print(f"Tipo: {tipo}, Precio por noche: ${precio}")

    def registrar_cliente(self):
        # Solicita al cliente su nombre y muestra las habitaciones disponibles
        nombre = input("Ingrese su nombre: ")
        self.mostrar_habitaciones()
        
        # Solicita al cliente que elija un tipo de habitación
        habitacion_elegida = input("Elija el tipo de habitación: ")
        
        # Verifica si el tipo de habitación es válido
        if habitacion_elegida not in self.habitaciones:
            print("Tipo de habitación no válido. Intente nuevamente.")
            return
        
        # Solicita el número de noches que el cliente permanecerá en el hotel
        noches = int(input("Ingrese el número de noches que permanecerá: "))
        
        # Calcula el total inicial multiplicando el precio de la habitación por el número de noches que estará en el hotel
        total = self.habitaciones[habitacion_elegida] * noches

        # Muestra los servicios extra disponibles y sus costos
        print("\nServicios extra disponibles:")
        for servicio, costo in self.servicios_extra.items():
            print(f"Servicio: {servicio}, Costo: ${costo}")
        
        # Solicita al cliente que elija los servicios extra
        servicios_seleccionados = input("Ingrese los servicios extra separados por coma (piscina, cancha de Golf), o 'ninguno' si no desea servicios extra: ").split(", ")
        
        # Agrega el costo de cada servicio extra seleccionado al total
        for servicio in servicios_seleccionados:
            if servicio in self.servicios_extra:
                total += self.servicios_extra[servicio]
            elif servicio.lower() == 'ninguno':
                break
            else:
                print(f"Servicio {servicio} no válido.")
        
        # Creamos otro diccionario que representa la factura del cliente
        factura = {
            "nombre": nombre,
            "habitacion": habitacion_elegida,
            "noches": noches,
            "servicios_extra": servicios_seleccionados,
            "total": total
        }
        
        # Almacena la factura en la lista de facturas
        self.facturas.append(factura)
        
        # Muestra la factura al cliente
        self.mostrar_factura(factura)

    def mostrar_factura(self, factura):
        # Muestra los detalles de la factura generada para el cliente
        print("\n--- Factura ---")
        print(f"Nombre: {factura['nombre']}")
        print(f"Habitación: {factura['habitacion']}")
        print(f"Noches: {factura['noches']}")
        print("Servicios extra:", ", ".join(factura["servicios_extra"]) if factura["servicios_extra"] else "Ninguno")
        print(f"Total a pagar: ${factura['total']}")
        print("----------------\n")


hotel = Hotel()

# Bucle principal del programa
while True:
    print("\n--- Hotel de Playa ---")
    print("1. Registrar nuevo cliente")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    # Opción para registrar un nuevo cliente.
    if opcion == "1":
        hotel.registrar_cliente()
    # Opción para salir del programa.
    elif opcion == "2":
        print("Saliendo del programa...")
        break
    # Manejo de opciones inválidas.
    else:
        print("Opción no válida. Intente nuevamente.")
