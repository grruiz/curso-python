def muestraNombres():
    print("Rafael")

muestraNombres()

nombre = "Rafael"

def mostrarTunombre(nombre="Rafa"):
    print("Tu nombre es: {nombre} ")


mostrarTunombre()

#Parametros opcionales
def getEmpleado(nombre,dni = "asdkoas"):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"Nombre: {dni}")


getEmpleado("Rafael")


#Lambda
tellMeYear = lambda year: f"El año es {year * 50}"

print(tellMeYear(2035))