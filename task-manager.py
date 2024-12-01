### Author: Guillermo Ayllon ###
### Date: 01/12/2024 ###

###################################################################

class Tarea:
    """
    Clase que representa una tarea individual.
    """
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True

    def __str__(self):
        """
        Representación en texto de la tarea, mostrando su estado.
        """
        estado = "Completada" if self.completada else "Pendiente"
        return f"[{estado}] {self.descripcion}"


class GestorDeTareas:
    """
    Clase para gestionar una lista de tareas pendientes.
    """
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """
        Agrega una nueva tarea a la lista de tareas.
        """
        self.tareas.append(Tarea(descripcion))
        print(f"Tarea '{descripcion}' agregada con éxito.")

    def marcar_tarea_completada(self, indice):
        """
        Marca una tarea como completada dado su índice.
        """
        try:
            self.tareas[indice].marcar_completada()
            print(f"Tarea '{self.tareas[indice].descripcion}' marcada como completada.")
        except IndexError:
            print("Error: Índice fuera de rango. Por favor, intente de nuevo.")

    def mostrar_tareas(self):
        """
        Muestra todas las tareas con su estado y posición en la lista.
        """
        if not self.tareas:
            print("No hay tareas pendientes.")
            return
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"{i}. {tarea}")

    def eliminar_tarea(self, indice):
        """
        Elimina una tarea dado su índice.
        """
        try:
            tarea_eliminada = self.tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada con éxito.")
        except IndexError:
            print("Error: Índice fuera de rango. Por favor, intente de nuevo.")


def menu():
    """
    Función principal que muestra el menú de opciones al usuario.
    """
    gestor = GestorDeTareas()
    while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Agregar una nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                descripcion = input("Ingrese la descripción de la nueva tarea: ")
                gestor.agregar_tarea(descripcion)
            elif opcion == 2:
                gestor.mostrar_tareas()
                indice = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
                gestor.marcar_tarea_completada(indice)
            elif opcion == 3:
                gestor.mostrar_tareas()
            elif opcion == 4:
                gestor.mostrar_tareas()
                indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
                gestor.eliminar_tarea(indice)
            elif opcion == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número.")


if __name__ == "__main__":
    menu()
