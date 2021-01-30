"""
Modulos: son funcionalidad ya hechas para reutilizar.
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, o crear nuestro propios modulos.
"""
# Importamos nuestro modulo
# import modulo
from modulo import holaMundo #Importamos el metodo que nos interesa de ese modulo

#print(modulo.holaMundo("Rafa"))
print(holaMundo("Rafa"))


import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")#Formatear la fecha
print(f"Mi fecha personalizada {fecha_personalizada}")

print(datetime.datetime.now().time())

#Modulo matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Numero PI: ", float(math.pi))
print("Redondear: ",math.floor(6.45432))

#Modulo random

import random

print("Numero aleatorio: ", random.randint(15,54))