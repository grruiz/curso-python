#Capturar excepciones y manejar errores en codigo 
# susceptible a fallos/errores

"""
try:
    nombre = input("Cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es "+ nombre


    print(nombre_usuario)
except:
    print("Ha ocurrido un error, introduce bien tu nombre ")
else:
    print("Todo ha funcionado correctamente")
finally: 
    print("Fin de la iteracion")
"""
"""
#Multiples excepciones
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print(f"El cuadrado es {numero*numero}")
except TypeError: 
    print("Debes convertir tus cadenas a enteros")
#except ValueError:
 #   print("Introduce un numero correcto")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)
"""

#Excepciones personalizadas o lanzar excepcion
try:
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta correcto")
    else:
        print("Bienvenido")
except ValueError:
    print("Introduce un valor correcto")
except Exception as e:
    print("Ha ocurrido algun error" +e)