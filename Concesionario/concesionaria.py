"""Módulo que define la clase Concesionaria para gestionar vehículos.

Permite agregar vehículos de diferentes tipos (Auto, Moto, Camión),
mostrar su catálogo completo y calcular el total de la concesionaria.
"""

class Concesionaria:
    """Clase que representa una concesionaria de vehículos."""

    def __init__(self):
        """Inicializa la concesionaria con una lista vacía de vehículos."""
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        """
        Agrega un vehículo a la concesionaria.

        Args:
        vehiculo (Vehiculo): Instancia de Vehiculo o cualquiera de sus clases hijas 
        (Auto, Moto, Camión).
        Acción:
            - Aplica polimorfismo al llamar a vehiculo.descripcion() sin importar su tipo.
            - Muestra mensaje indicando que se agregó el vehículo con su precio.
        """

        print(
            f"Agregado: {vehiculo.descripcion()} - Precio: "
            f"${vehiculo.get_precio()}"
        )
        #Dividir la línea usando paréntesis para que quede más corta
        #Por lo que cada línea queda por debajo de 100 caracteres y Pylint no marcará el error.
        self.vehiculos.append(vehiculo)

    def mostrar_catalogo(self):
        """
        Muestra todos los vehículos en la concesionaria y calcula el total.

        Acción:
            - Recorre la lista de vehículos y llama a descripcion() de cada uno (polimorfismo).
            - Suma los precios usando get_precio() (encapsulamiento).
            - Imprime el total acumulado de la concesionaria.
        """

        print("--- Catálogo de Vehículos ---")
        total = 0
        for v in self.vehiculos:
            # Llamada a metodo descripcion() de cada vehículo (polimorfismo)
            print(
                f"{v.descripcion()} | "
                f"${v.get_precio()}"
            )
            # Sumar el precio del vehículo al total
            total += v.get_precio()
        # Muestra el valor total de todos los vehiculos de la consesionaria
            #si pongo este print dentro del bucle me mostrara valores acumativos
            #print(f"Valor total de vehiculos en la concesionaria: ${total}")
        print(f"Valor total de vehiculos en la concesionaria: ${total}")
