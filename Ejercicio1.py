class ConsultorioMedico:
    def __init__(self):
        
        self.pacientes = {}

    def registrar_paciente(self, nombre, motivo_consulta):
        if nombre in self.pacientes:
            print(f"El paciente {nombre} ya tiene una consulta asignada para el día {self.pacientes[nombre]['fecha_consulta']}.")
            print("Por favor, pase a la sala de espera.")
        else:
            fecha_consulta = input("Ingrese la fecha de la consulta: ")
            self.pacientes[nombre] = {
                "motivo_consulta": motivo_consulta,
                "fecha_consulta": fecha_consulta
            }
            print(f"Consulta asignada a {nombre} para el día {fecha_consulta}.")

    def mostrar_pacientes(self):
        print("Pacientes registrados:")
        for nombre, datos in self.pacientes.items():
            print(f"Nombre: {nombre}, Motivo: {datos['motivo_consulta']}, Fecha: {datos['fecha_consulta']}")


consultorio = ConsultorioMedico()

while True:
    print("\n--- Consultorio Médico ---")
    print("1. Registrar nuevo paciente")
    print("2. Mostrar pacientes registrados")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        motivo = input("Ingrese el motivo de la consulta: ")
        consultorio.registrar_paciente(nombre, motivo)
    elif opcion == "2":
        consultorio.mostrar_pacientes()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
