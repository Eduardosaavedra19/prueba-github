"""
Módulo que define la clase VehiculoCamion, heredando de Vehiculo, 
con atributos específicos para camiones.
"""

from vehiculo import Vehiculo


class VehiculoCamion(Vehiculo):
    """
    Clase que representa un vehículo tipo camión, con atributos como
    tipo, marca, modelo, precio y capacidad de carga.
    """

    def __init__(self, tipo, marca, modelo, precio, capacidad_carga):
        """
        Inicializa un VehiculoCamion.

        Args:
            tipo (str): Tipo de vehículo.
            marca (str): Marca del vehículo.
            modelo (str): Modelo del vehículo.
            precio (float): Precio del vehículo.
            capacidad_carga (float): Capacidad de carga del camión en toneladas o kilogramos.
        """
        super().__init__(tipo, marca, modelo, precio)
        self.capacidad_carga = capacidad_carga

    def descripcion(self):
        """
        Devuelve una descripción completa del camión.
        """
        return (f"Vehiculo tipo {self.tipo}, marca {self.marca}, modelo {self.modelo} "
                f"y con capacidad de carga de {self.capacidad_carga}")
#Dividir la línea usando paréntesis para que quede más corta
#Por lo que cada línea queda por debajo de 100 caracteres y Pylint no marcará el error.
