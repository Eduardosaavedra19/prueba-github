from Sandwich import Sandwich

class Sandwich_Vegetariano(Sandwich):
    def __init__(self, pan, precio, verduras):
        super().__init__(pan, precio)
        self.verduras = verduras
        
    def descripcion(self):
        return f"Sandwich Vegeteriano con pan {self.pan} y verduras {self.verduras}"