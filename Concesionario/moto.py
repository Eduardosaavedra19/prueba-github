"""
Módulo que define la clase VehiculoMoto, heredando de Vehiculo,
con atributos específicos para motocicletas.
"""

from vehiculo import Vehiculo


class VehiculoMoto(Vehiculo):
    """
    Clase que representa un vehículo tipo moto, con atributos como
    tipo, marca, modelo, precio y cilindrada.
    """

    def __init__(self, tipo, marca, modelo, precio, cilindrada):
        """
        Inicializa un VehiculoMoto.

        Args:
            tipo (str): Tipo de vehículo.
            marca (str): Marca del vehículo.
            modelo (str): Modelo del vehículo.
            precio (float): Precio del vehículo.
            cilindrada (int): Cilindrada de la motocicleta.
        """
        super().__init__(tipo, marca, modelo, precio)
        self.cilindrada = cilindrada

    def descripcion(self):
        """
        Devuelve una descripción completa de la motocicleta.
        """
        return (f"Vehiculo tipo {self.tipo}, marca {self.marca}, modelo {self.modelo} "
                f"de {self.cilindrada} cilindrada")
    #Dividir la línea usando paréntesis para que quede más corta
    #Por lo que cada línea queda por debajo de 100 caracteres y Pylint no marcará el error.
    