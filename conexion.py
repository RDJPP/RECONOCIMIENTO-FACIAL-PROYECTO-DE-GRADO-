
import mysql.connector

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='base_datos', 
                                            user = 'root',
                                            password ='Heliumred1@')


    def inserta_producto(self,cedula, nombre, apellido, telefono, direccion):
        cur = self.conexion.cursor()
        sql='''INSERT INTO productos (CEDULA, NOMBRE, APELLIDO, TELEFONO, DIRECCION) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(cedula, nombre, apellido, telefono, direccion)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 


    def elimina_productos(self, nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM productos WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
  
    def actualiza_productos(self,Id, cedula, nombre, apellido, telefono, direccion):
        cur = self.conexion.cursor()
        sql ='''UPDATE productos SET  CEDULA ='{}', NOMBRE = '{}' , APELLIDO = '{}', TELEFONO = '{}', DIRECCION = '{}'
        WHERE ID = '{}' '''.format(cedula, nombre, apellido, telefono, direccion, Id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a  
