#- Eduardo Saavedra 
#	-Juego
#		-atributos:
#			nombre: string "piña movil"
#			genero: string "indie"
#			precio: string "2 us" 
#			plataforma: string "movil"
#		-Metodos:
#			guardar ()
#			cargar ()
#			iniciar ()
#			acciones ()

class Juego:
    
    def __init__(self, Nombre, Genero, Precio, Plataforma):
                     
        self.Nombre = Nombre
        self.Genero = Genero
        self.Precio = Precio
        self.Plataforma = Plataforma
        self.iniciar_juego = False
           
    def iniciar(self):
        self.iniciar_juego = True
        return f"El {self.Nombre} a iniciado"
    

        
    
