"""
FOR 
"""
contador = 0
resultado = 0
for contador in range(0,5):
    print("Voy por el "+str(contador))
    
    resultado += contador

print(f"El resultado es: {resultado} ")

#Tabla multiplicar
numeroUsuario = int(input("De que numero quieres la tabla: "))
if numeroUsuario < 1:
    numeroUsuario = 1

print(f"Tabla de multiplicar de numero {numeroUsuario} ")

for numero_tabla in range(1,11):
    print(f"{numeroUsuario} x {numero_tabla} = {numeroUsuario*numero_tabla} ")
else:
    print("Tabla finalizada")