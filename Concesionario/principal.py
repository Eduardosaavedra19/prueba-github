"""Clase principal para ejecutar la concesionaria"""

from auto import VehiculoAuto
from camion import VehiculoCamion
from concesionaria import Concesionaria
from moto import VehiculoMoto

# Crear la concesionaria
mi_concesionaria = Concesionaria()

# Instanciar un auto, una moto y un camión (se crea el objeto)
#auto = VehiculoAuto("Auto", "Toyota", "Corolla", 15000000, 4)
#moto = VehiculoMoto("Moto", "Honda", "CBR", 5000000, 600)
#camion = VehiculoCamion("Camión", "Volvo", "FH", 60000000, "20 toneladas")

# Usar el setter para modificar el precio de uno de ellos
#moto.set_precio(5500000)   # cambiamos el precio de la moto

# Agregar los vehículos a la concesionaria
#mi_concesionaria.agregar_vehiculo(auto)
#mi_concesionaria.agregar_vehiculo(moto)
#mi_concesionaria.agregar_vehiculo(camion)

# Esto es en caso de agregar varios vehiculos
# creo que es mas realista para practicar
autos = [
    VehiculoAuto("Auto", "Toyota", "Corolla", 15000000, 4),
    VehiculoAuto("Auto", "Ford", "Focus", 14000000, 4),
    VehiculoAuto("Auto", "Chevrolet", "Cruze", 14500000, 4)
]

motos = [
    VehiculoMoto("Moto", "Honda", "CBR", 5000000, 600),
    VehiculoMoto("Moto", "Yamaha", "R3", 4800000, 500),
    VehiculoMoto("Moto", "Suzuki", "GSX", 5100000, 650)
]

camiones = [
    VehiculoCamion("Camión", "Volvo", "FH", 60000000, "20 toneladas"),
    VehiculoCamion("Camión", "Scania", "R500", 62000000, "18 toneladas"),
    VehiculoCamion("Camión", "Mercedes", "Actros", 61000000, "22 toneladas")
]

# Usar el setter para modificar el precio de dos de ellos
# ma primera moto
motos[0].set_precio(5500000)
camiones[2].set_precio(80000000)

# Agregar todos a la concesionaria
for v in autos + motos + camiones:
    mi_concesionaria.agregar_vehiculo(v)

# Mostrar el catálogo completo
mi_concesionaria.mostrar_catalogo()
