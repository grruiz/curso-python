"""
Ejercicio 1 
        - Crear variables una pais y otra continente
        - Mostrar su valor por pantalla 
        - Poner un comentario con el tipo de dato
"""

pais = input("Introduce tu pais: ")
continente = input("Introduce tu continente: ")
year = int(input("Introduce el año al que estamos: "))

if(pais == "Spain" and continente == "Europe"):
    print("Eres Europeo")
else:
    print("No eres de este continente")

print(f"{pais} - {continente} - {year} ")
print(f"Pais {type(pais)} - Pais {type(pais)} - Año {type(year)}")