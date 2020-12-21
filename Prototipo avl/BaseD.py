import Tabla

class bd:
    def __init__(self):
        self.idTabla = None
        self.arvolTabla = Tabla()
    
    def crear(self, valor):
        self.arvolTabla.add(valor)
    
    def borrar(self, valor):
        self.arvolTabla.Eliminar(valor)