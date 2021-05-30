import sqlite3
#Creo un archivo base de dato tipo sqlite
miConexion =sqlite3.connect("PrimeraBase")
miCursor = miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") #SE COMENTA UNA VEZ CREADO LA BASE

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")
#variosProductos=[
#	("Porter", 300, "470cc"),
#	("Dorada Pampeana", 600, "600cc"),
#	("Scottish", 900,"970cc")
#]

#miConexion.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)
miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductosIn= miCursor.fetchall()
for producto in variosProductosIn:
		print("Nombre Articulo: ", producto[0], "seccion: ", producto[2])
miConexion.commit()
miConexion.close()