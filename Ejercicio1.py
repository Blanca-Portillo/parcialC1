class ConsultorioMedico:
    def __init__(self):
        # Inicializa un diccionario vacío para almacenar los pacientes y sus datos
        self.pacientes = {}

    def registrar_paciente(self, nombre, motivo_consulta):
        # Verifica si el paciente ya está registrado
        if nombre in self.pacientes:
            # Si ya tiene una consulta asignada, informa al paciente y lo dirige a la sala de espera
            print(f"El paciente {nombre} ya tiene una consulta asignada para el día {self.pacientes[nombre]['fecha_consulta']}.")
            print("Por favor, pase a la sala de espera.")
        else:
            # Si no tiene una consulta previa solicita la fecha de la consulta y registra al paciente
            fecha_consulta = input("Ingrese la fecha de la consulta: ")
            self.pacientes[nombre] = {
                "motivo_consulta": motivo_consulta,
                "fecha_consulta": fecha_consulta
            }
            # Confirma la asignación de la consulta
            print(f"Consulta asignada a {nombre} para el día {fecha_consulta}.")

    def mostrar_pacientes(self):
        # Muestra la lista de pacientes registrados junto con sus motivos de consulta y fechas
        print("Pacientes registrados:")
        for nombre, datos in self.pacientes.items():
            print(f"Nombre: {nombre}, Motivo: {datos['motivo_consulta']}, Fecha: {datos['fecha_consulta']}")

# Crea una instancia de la clase ConsultorioMedico
consultorio = ConsultorioMedico()

# Bucle principal para el menú de opciones
while True:
    print("\n--- Consultorio Médico ---")
    print("1. Registrar nuevo paciente")
    print("2. Mostrar pacientes registrados")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    # Opción para registrar un nuevo paciente
    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        motivo = input("Ingrese el motivo de la consulta: ")
        consultorio.registrar_paciente(nombre, motivo)
    
    # Opción para mostrar la lista de pacientes registrados
    elif opcion == "2":
        consultorio.mostrar_pacientes()
    
    # Opción para salir del programa
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    
    # Manejo de opciones inválidas
    else:
        print("Opción no válida. Intente nuevamente.")
