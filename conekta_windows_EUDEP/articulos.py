import sqlite3

class Articulos:

    def abrir(self):
        #conexion=sqlite3.connect("c:/Users/Iván/Desktop/conekta_windows/bd1.db")
        conexion=sqlite3.connect("oxxo.db")
        return conexion

    # PAGINA 1
    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into general(cliente, telefono, correo, direccion, tipo_pago, monto, monto_vista, fecha_creacion) values (?,?,?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def referencias(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into ref_conekta(order_id, tipo_pago, referencia_oxxo, monto, tipo_valor) values (?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    # PAGINA 2
    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql= "select cliente, telefono, correo, direccion, tipo_pago, monto, monto_vista, fecha_creacion from general order by id desc limit 0, ?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    # PAGINA 3
    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            #sql="select codigo, cliente, monto, telefono, correo, direccion from general UNION select codigo, cliente, monto, telefono, correo, direccion from examen"
            sql="SELECT a.cliente, a.telefono, a.correo, a.direccion, a.tipo_pago, a.monto, a.fecha_creacion, b.order_id, b.referencia_oxxo FROM general a LEFT JOIN ref_conekta b ON a.id = b.id"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
