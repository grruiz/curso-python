#Programación orientada a objetos(POO o OPP)

class Coche: 
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

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

#Crear objeto
coche = Coche()

print(coche.marca, coche.color)
print("Velocidad actual: ",coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print("Velocidad nueva: ", coche.velocidad)