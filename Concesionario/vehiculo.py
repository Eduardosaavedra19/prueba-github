"""
Módulo que define la clase Vehiculo, base para otros tipos de vehículos.
"""

class Vehiculo:
    """
    Clase base que representa un vehículo genérico con atributos como
    tipo, marca, modelo y precio.
    """

    def __init__(self, tipo, marca, modelo, precio):
        """
        Inicializa un Vehiculo.

        Args:
            tipo (str): Tipo de vehículo.
            marca (str): Marca del vehículo.
            modelo (str): Modelo del vehículo.
            precio (float): Precio del vehículo (debe ser mayor a 0).
        """
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio

    def get_precio(self):
        """
        Getter que devuelve el precio del vehículo.

        Returns:
            float: Precio del vehículo.
        """
        return self.__precio

    def set_precio(self, nuevo_precio):
        """
        Setter que modifica el precio del vehículo.

        Args:
            nuevo_precio (float): Nuevo precio del vehículo. Debe ser mayor que 0.
        """
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El nuevo precio debe ser mayor que 0")

    def descripcion(self):
        """
        Método que devuelve una descripción del vehículo.
        Este método puede ser sobreescrito por clases hijas.

        Returns:
            str: Descripción del vehículo.
        """
        return f"Vehiculo tipo {self.tipo}, marca {self.marca} y modelo {self.modelo}"
