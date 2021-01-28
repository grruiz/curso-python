"""
Numero pares del 1 al 100
"""

numero = 0

while numero <= 100:
    if(numero % 2 == 0):
        print(f"El numero {numero} : Es par")
    else: 
        print(f"El numero {numero} : No es par")
    numero += 1