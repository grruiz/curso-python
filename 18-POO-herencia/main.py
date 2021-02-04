import clases

persona = clases.Persona()
persona.setNombre("Rafael")
persona.setApellidos("Galvez Ruiz")
persona.setAltura("190cm")
persona.setEdad("231")

print(f"Nombre: {persona.getNombre()}")

informatico = clases.Informatico()
informatico.setNombre("Rafa")
informatico.setApellidos("El informatico")
print(f"Nombre: {informatico.getNombre()}")