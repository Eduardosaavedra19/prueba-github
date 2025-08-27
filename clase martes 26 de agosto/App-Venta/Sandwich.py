class Sandwich:

    def __init__(self, pan, precio):
    
        self.pan = pan
        self.__precio = precio

# getter (me entrega el precio)
    def get_precio(self):
        return self.__precio
    
#setter (modifica el precio)
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que 0")

#metodo que sera sobreescrito con polimorfismo

    def descripcion(self):
        return f"Sandwich con pan {self.pan}"
