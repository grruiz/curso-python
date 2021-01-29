nombre = "Rafael"

#Funciones generales
print(type(nombre))


#Detectar tipado
comprobar = isinstance(nombre,str)

if comprobar: 
    print("Es un String")
else:
    print("No es una cadena")


if not isinstance(nombre,float):
    print("La variable no es un float")

#Limpiar espacios
frase = "       mi contenido      "
print(frase.strip()) 

#Elimar variables
year = 2021
print(year)
del year
#print(year)

#Comprobar variable vacia
texto = "  ff  "

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido", len(texto))

#Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

#Reemplazara palabras en 
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())