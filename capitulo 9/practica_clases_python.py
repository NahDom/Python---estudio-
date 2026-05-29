"""definicion de clases"""

class Dispositivo:
    # metodo constructor
    def __init__(self, IP):
        self.IP =  IP
        self.encendido = False
    # metodo destructor
    def __del__(self):
        print("destruyendo el objeto instanciado previamente")
        
    def encender(self):
        self.encendido = True
    
    def apagar(self):
        self.encendido = False
    
    def estado(self):
        mensaje = f"IP:{self.IP}"
        
        if self.encendido:
            mensaje += 'Estado: encendido\n'
        else:
            mensaje += 'Estado: apagado\n'
        return mensaje
# instanciamos la clase
