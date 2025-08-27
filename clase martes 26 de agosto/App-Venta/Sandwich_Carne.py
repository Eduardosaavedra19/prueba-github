from Sandwich import Sandwich

class Sandwich_Carne(Sandwich):
    def __init__(self, pan, precio, carne, queso):
        super().__init__(pan, precio)
        self.carne = carne
        self.queso = queso
        
    def descripcion(self):
        return f"Sandwich Vegeteriano con pan {self.pan}, carne {self.carne} y queso {self.queso}"
