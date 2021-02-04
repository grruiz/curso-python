#Programación orientada a objetos(POO o OPP)

class Coche: 
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    __privado = "Esta variable es privada"


    def __init__(self, color,marca,modelo,velocidad,caballe,plazas):
        self.color = color 
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballe
        self.plazas = plazas

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self,modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):
        info = "--------- Informacio del coche --------"
        info += "\n Color: "+ self.getColor()
        info += "\n Modelo: "+ self.getModelo()
        return info