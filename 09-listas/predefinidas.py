cantantes = ['Drake','Alfredo','Eustavio']
numeros = [1,2,3,4,8,20,5,30]

#Ordenar lista
numeros.sort()
print(numeros)

# Add elements
cantantes.append("Estrella")
cantantes.insert(0,"Willyrex") #Insertamos en la posicion que queramos
print(cantantes)


#Eliminar elementos
cantantes.pop(1)
cantantes.remove('Eustavio')
print(cantantes)

#Dar la vuelta a una lista
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Estrella' in cantantes)

#Contar elementos
print(len(cantantes))

# Cuantas veces un elemento
numeros.append(30)
print(numeros.count(30))

#Conseguir indice
print(cantantes.index("Estrella"))

#Unir listas
cantantes.extend(numeros)
print(cantantes)