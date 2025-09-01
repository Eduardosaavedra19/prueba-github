"""
Módulo que define la clase VehiculoAuto, heredando de Vehiculo, 
con atributos específicos para automóviles.
"""

from vehiculo import Vehiculo


class VehiculoAuto(Vehiculo):
    """
    Clase que representa un vehículo tipo auto, con atributos como
    tipo, marca, modelo, precio y número de puertas.
    """

    def __init__(self, tipo, marca, modelo, precio, puertas):
        """
        Inicializa un VehiculoAuto.

        Args:
            tipo (str): Tipo de vehículo.
            marca (str): Marca del vehículo.
            modelo (str): Modelo del vehículo.
            precio (float): Precio del vehículo.
            puertas (int): Número de puertas del automóvil.
        """
        super().__init__(tipo, marca, modelo, precio)
        self.puertas = puertas

    def descripcion(self):
        """
        Devuelve una descripción completa del vehículo.
        """
        return (f"Vehiculo tipo {self.tipo}, marca {self.marca}, "
                f"modelo {self.modelo} de {self.puertas} puertas")
    #Dividir la línea usando paréntesis para que quede más corta
    #Por lo que cada línea queda por debajo de 100 caracteres y Pylint no marcará el error.
