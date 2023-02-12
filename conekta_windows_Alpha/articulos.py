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
        sql="insert into general(id_cliente, no_pedido, importe, orden_venta, orden_venta_d, correo, concepto, importe_2, fecha_carga, titular, membresia) values (?,?,?,?,?,?,?,?,?,?,?)"
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
            #sql= "select a.cliente, a.telefono, a.correo, a.direccion, a.tipo_pago, a.monto, a.fecha_creacion, b.referencia_oxxo from general a LEFT JOIN ref_conekta b on (a.id = b.id) order by a.id desc limit 0, ?"
            sql = "SELECT fecha_carga ,id_cliente, no_pedido, importe, importe_2, orden_venta, orden_venta_d, correo, concepto, titular, membresia FROM general order by id desc limit 0, ?"
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

    # PAGINA 4
    def consulta_mail(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql= "SELECT a.fecha_carga ,a.id_cliente, a.importe, a.importe_2, a.correo, a.titular, b.referencia_oxxo FROM general a LEFT JOIN ref_conekta b on (a.id = b.id) order by a.id DESC LIMIT 0, ?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
