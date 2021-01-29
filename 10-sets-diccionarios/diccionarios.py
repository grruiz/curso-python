"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato de clave valor.
Es parecio a un array asociativo o un objeto json.
"""

persona = {
    "nombre":"Rafael",
    "apellidos":"Galvez",
    "web":"melainvento.com"
}

print(persona["apellidos"])


# Lista con diccionarios
contactos = [
    {
        'nombre':'Rafael',
        'email': 'rafael@rafael'

    },
    {
        'nombre':'Luis',
        'email':'luis@luis'
    },
    {
        'nombre':'Salvador',
        'email':'salvador@salvador'
    }
]

print(contactos[0]['nombre'])

print("Lista de contactos")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("\n")