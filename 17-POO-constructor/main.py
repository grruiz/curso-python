from coche import Coche

carro = Coche("Amarillo","Renault","Coche",200,4,3)
print(carro.getInfo())

if type(carro) == Coche:
    print("Es un objeto coche")
else:
    print("No es un objeto coche")


# Visibilidad 
