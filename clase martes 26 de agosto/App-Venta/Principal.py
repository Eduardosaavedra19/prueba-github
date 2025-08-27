from Sandwich import Sandwich
from Ventas import Venta
from Sandwich_Carne import Sandwich_Carne
from Sandwich_Vegetariano import Sandwich_Vegetariano

mi_sandwich = Sandwich("blanco", 2000)
Ventas = Venta()

vegetariano = Sandwich_Vegetariano("centeno", 2000, "tomate, lechuga") 
carne = Sandwich_Carne( "ciabata", 3000, "churrasco", "cheddar")

# agregar pédidos

Ventas.agregar_sandwich(vegetariano)
Ventas.agregar_sandwich(carne)

Ventas.mostrar_venta()
