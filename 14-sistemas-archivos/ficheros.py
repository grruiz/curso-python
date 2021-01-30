from io import open # Libreria para manejar archivos
import pathlib

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

# Escribir en un archivo

archivo.write("***Texto Ejemplo***\n")

#Cerrar archivo
archivo.close()