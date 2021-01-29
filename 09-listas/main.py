"""
LISTAS O ARRAYS 
son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice numerico.
"""

pelicula = "Batman"
#Definir lista
peliculas = ["Batman","Spiderman","Porky"]
cantantes = list(("2pac","Drake","JLO"))    
years = list(range(2000,2020))
variada = ["Rafael", 30,4.5,True,"Texto"]
#print(variada)

# Indices
peliculas[2] = "Torino" #Cambio el contenido 
print(peliculas[0])
print(peliculas[-2]) #Con esto empieza de final al inicio
print(cantantes[1:3]) #Recorre un rango del 1 al 3
print(peliculas[1:]) #Empieza a partir del 1

# Añadir elementos a lista
cantantes.append("Kase O")
print(cantantes)

# Recorrer Lista
"""
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f" {peliculas.index(pelicula)+1}. {pelicula}")
"""

# Lista multidimensionales
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        print(elemento)
    print("\n")

print(contactos[1][1])