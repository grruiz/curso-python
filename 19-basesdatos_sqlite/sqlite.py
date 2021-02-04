import sqlite3

#Conexion
conexion = sqlite3.connect('pruebas.db')

#Crear cursor 
cursor = conexion.cursor()
#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(255), "+
"descripcion TEXT,"+
"precio int(255)"+
")")

#Guardar cambios
conexion.commit()

#Insertar datos
#cursor.execute("INSERT INTO productos VALUES (null,'Primer producto','descripcion',550)")
#conexion.commit()

#Insertar muchos productos en la tabla de la base de datos
productos = [
    ("Ordenador","Buen PC",700),
    ("Movil","Buen PC",200),
    ("Placa base","Buen PC",300),
]


cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos)
conexion.commit()

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

#Borrar registros

for producto in productos:
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

#cerrar conexion
conexion.close()