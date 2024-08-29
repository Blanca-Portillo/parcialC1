from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.en_prestamo = False


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

class SistemaBiblioteca:
    def __init__(self):
        self.registro_prestamos = {}

    def prestar_libro(self, persona, libro, dias_prestamo):
        if Libro.en_prestamo:
            print(f"El libro '{Libro.titulo}' ya está en préstamo.")
            return

        fecha_actual = datetime.now()
        fecha_devolucion = fecha_actual + timedelta(days=dias_prestamo)

        self.registro_prestamos[libro] = {
            "persona": persona,
            "fecha_prestamo": fecha_actual,
            "fecha_devolucion": fecha_devolucion
        }
        Libro.en_prestamo = True
        Persona.libros_prestados.append(libro)

        print(f"Libro '{Libro.titulo}' prestado a {Persona.nombre} hasta {fecha_devolucion.strftime}.")

    def devolver_libro(self, persona, libro):
        if libro not in self.registro_prestamos:
            print(f"El libro '{Libro.titulo}' no está registrado como prestado.")
            return

        datos_prestamo = self.registro_prestamos[libro]
        fecha_actual = datetime.now()

        if fecha_actual > datos_prestamo["fecha_devolucion"]:
            print(f"El libro '{Libro.titulo}' ha sido devuelto tarde. Se aplicará una sanción.")
        else:
            print(f"Libro '{Libro.titulo}' devuelto a tiempo por {Persona.nombre}.")

        Libro.en_prestamo = False
        Persona.libros_prestados.remove(libro)
        del self.registro_prestamos[libro]





