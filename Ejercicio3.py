class Hotel:
    def __init__(self):
    
        self.habitaciones = {
            "simple": 100,
            "doble": 150,
            "suite": 250
        }
       
        self.servicios_extra = {
            "piscina": 20,
            "cancha de Golf": 50
        }
       
        self.facturas = []

    def mostrar_habitaciones(self):
        print("Habitaciones disponibles:")
        for tipo, precio in self.habitaciones.items():
            print(f"Tipo: {tipo}, Precio por noche: ${precio}")

    def registrar_cliente(self):
        nombre = input("Ingrese su nombre: ")
        self.mostrar_habitaciones()
        habitacion_elegida = input("Elija el tipo de habitación: ")
        
        if habitacion_elegida not in self.habitaciones:
            print("Tipo de habitación no válido. Intente nuevamente.")
            return
        
        noches = int(input("Ingrese el número de noches que permanecerá: "))
        total = self.habitaciones[habitacion_elegida] * noches

        print("\nServicios extra disponibles:")
        for servicio, costo in self.servicios_extra.items():
            print(f"Servicio: {servicio}, Costo: ${costo}")
        
        servicios_seleccionados = input("Ingrese los servicios extra separados por coma  piscina, cancha de Golf), o 'ninguno' si no desea servicios extra: ").split(", ")
        
        for servicio in servicios_seleccionados:
            if servicio in self.servicios_extra:
                total += self.servicios_extra[servicio]
            elif servicio.lower() == 'ninguno':
                break
            else:
                print(f"Servicio {servicio} no válido.")

        
        factura = {
            "nombre": nombre,
            "habitacion": habitacion_elegida,
            "noches": noches,
            "servicios_extra": servicios_seleccionados,
            "total": total
        }
        self.facturas.append(factura)
        self.mostrar_factura(factura)

    def mostrar_factura(self, factura):
        print("\n--- Factura ---")
        print(f"Nombre: {factura['nombre']}")
        print(f"Habitación: {factura['habitacion']}")
        print(f"Noches: {factura['noches']}")
        print("Servicios extra:", ", ".join(factura["servicios_extra"]) if factura["servicios_extra"] else "Ninguno")
        print(f"Total a pagar: ${factura['total']}")
        print("----------------\n")

hotel = Hotel()

while True:
    print("\n--- Hotel de Playa ---")
    print("1. Registrar nuevo cliente")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        hotel.registrar_cliente()
    elif opcion == "2":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
