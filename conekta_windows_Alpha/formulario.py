import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
 #CONEKTA
import conekta
conekta.api_key = "key_xNJ1D5zpgMkBqy1Nnphmyg"    # Clave Privada
#conekta.api_key = "key_dQnVoYKS6m97vVt3a7zapcQ"  # Clave Publica
from datetime import datetime, timedelta
#thirty_days_from_now = int((datetime.now() + timedelta(days=1)).timestamp())
fecha = datetime.now()
import articulos
# API CLUB ALPHA
import requests
#import json
# CORREO
import smtplib
import email.message

class FormularioArticulos:
    def manual(self):
        mb.showinfo("Manual para Operación", 
                    "PASO 1: \nCARGAR DATOS CON EL ID DE CLIENTE.\n\nNecesitas el ID del Cliente y tener un cargo, de lo contrario no llenara los campos.\n\nEs importante que el cliente tenga correo asociado de lo contrario no podras generar la referencia de pago\n\n"
                    "PASO 2: \nENVIAR DATOS A OXXO.\n\nAl dar Clic al boton Cargar Datos, el sistema cargara el ultimo ID de Cliente del Paso 1.\n\nSi el Cliente no tiene Correo, no podras generar la referencia de pago.\n\n")
                    #"PASO 3: \nENVIAR DATOS AL CORREO DEL CLIENTE\n\nEnviar correo al cliente para que pueda realizar su pago Oxxo, con el N° de Referencia Generado")

    def soporte(self):
        mb.showinfo("Información", "Correo de Soporte:\nivan.najera@clubalpha.com.mx")

    def salir(self):
       self.ventana1.destroy()

    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Generador de Ordenes de Pago Oxxo")
        self.ventana1.geometry('1200x800')
        self.ventana1.config(bg ="gray")
        self.ventana1.config(bd="30")
        self.ventana1.config(relief="groove")
        # LIBRO
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.pago_general()
        self.carga_conekta()
        #self.enviar_correo_cliente()
        self.cuaderno1.grid(column=0, row=0, padx=180, pady=10)
        # MENU
        self.menu = Menu(self.ventana1)
        self.new_item = Menu(self.menu)
        self.new_item = Menu(self.menu, tearoff=0)
        self.new_item.add_command(label='Manual', command=self.manual)
        self.new_item.add_command(label='Soporte', command=self.soporte)
        self.new_item.add_separator()
        self.new_item.add_command(label='Salir', command=self.salir)
        self.menu.add_cascade(label='Herramientas', menu=self.new_item)
        # CONFIGURACION APP
        self.ventana1.config(menu=self.menu)
        self.ventana1.iconbitmap('icon.ico')
        self.ventana1.mainloop()

    # PAGINA 1
    def pago_general(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="PASO 1")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Carga Datos del Cliente")        
        self.labelframe1.grid(column=0, row=0, padx=220, pady=20)
        # FECHA DE CREACION
        self.label1=ttk.Label(self.labelframe1, text="Fecha de Carga:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.fechacarga=tk.StringVar(value=fecha)
        self.entryfecha=ttk.Entry(self.labelframe1, textvariable=self.fechacarga, width=30, justify='center')
        self.entryfecha.config(state='disabled')
        self.entryfecha.grid(column=1, row=1, padx=4, pady=4)
        # ID CLIENTE API
        self.label2=ttk.Label(self.labelframe1, text="ID CLIENTE:")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.api_cliente=tk.StringVar()
        self.entryapi_cliente=ttk.Entry(self.labelframe1, textvariable=self.api_cliente, width=30, justify='center')
        self.entryapi_cliente.config(state='enabled')
        self.entryapi_cliente.grid(column=1, row=2, padx=4, pady=4)
        # MEMBRESIA
        self.label11=ttk.Label(self.labelframe1, text="ID CLIENTE:")
        #self.label11.grid(column=0, row=2, padx=4, pady=4)
        self.api_membresia=tk.StringVar()
        self.entryapi_membresia=ttk.Entry(self.labelframe1, textvariable=self.api_membresia, width=30, justify='center')
        self.entryapi_membresia.config(state='disabled')
        #self.entryapi_membresia.grid(column=1, row=2, padx=4, pady=4)
        # N° DE PEDIDO API
        self.label3=ttk.Label(self.labelframe1, text="N° de Pedido:")
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.api_pedido=tk.StringVar()
        self.entryapi_pedido=ttk.Entry(self.labelframe1, textvariable=self.api_pedido, width=30, justify='center')
        self.entryapi_pedido.config(state='disabled')
        self.entryapi_pedido.grid(column=1, row=3, padx=4, pady=4)
        # IMPORTE API
        self.label4=ttk.Label(self.labelframe1, text="Importe:")
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.api_importe=tk.StringVar()
        self.entryapi_importe=ttk.Entry(self.labelframe1, textvariable=self.api_importe, width=30, justify='center')
        self.entryapi_importe.config(state='disabled')
        self.entryapi_importe.grid(column=1, row=4, padx=4, pady=4)
        # IMPORTE 2 API
        self.label5=ttk.Label(self.labelframe1, text="Importe:") # CONEKTA
        #self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.api_importe_2=tk.StringVar()
        self.entryapi_importe_2=ttk.Entry(self.labelframe1, textvariable=self.api_importe_2, width=30, justify='center')
        self.entryapi_importe_2.config(state='disabled')
        #self.entryapi_importe_2.grid(column=1, row=5, padx=4, pady=4)
        # ORDEN DE VENTA API
        self.label6=ttk.Label(self.labelframe1, text="Orden de Venta:")
        self.label6.grid(column=0, row=6, padx=4, pady=4)
        self.api_ov=tk.StringVar()
        self.entryapi_ov=ttk.Entry(self.labelframe1, textvariable=self.api_ov, width=30, justify='center')
        self.entryapi_ov.config(state='disabled')
        self.entryapi_ov.grid(column=1, row=6, padx=4, pady=4)
        # ORDEN DE VENTA DETALLE API
        self.label7=ttk.Label(self.labelframe1, text="Orden de Venta Detalle:")
        self.label7.grid(column=0, row=7, padx=4, pady=4)
        self.api_ovd=tk.StringVar()
        self.entryapi_ovd=ttk.Entry(self.labelframe1, textvariable=self.api_ovd, width=30, justify='center')
        self.entryapi_ovd.config(state='disabled')
        self.entryapi_ovd.grid(column=1, row=7, padx=4, pady=4)
        # CORREO ELECTRONICO API
        self.label8=ttk.Label(self.labelframe1, text="Correo Cliente:")
        self.label8.grid(column=0, row=8, padx=4, pady=4)
        self.api_correo=tk.StringVar()
        self.entryapi_correo=ttk.Entry(self.labelframe1, textvariable=self.api_correo, width=30, justify='center')
        self.entryapi_correo.config(state='disabled')
        self.entryapi_correo.grid(column=1, row=8, padx=4, pady=4)
        # CONCEPTO API
        self.label9=ttk.Label(self.labelframe1, text="Concepto:")
        self.label9.grid(column=0, row=9, padx=4, pady=4)
        self.api_concepto=tk.StringVar()
        self.entryapi_concepto=ttk.Entry(self.labelframe1, textvariable=self.api_concepto, width=30, justify='center')
        self.entryapi_concepto.config(state='disabled')
        self.entryapi_concepto.grid(column=1, row=9, padx=4, pady=4)
        # TITULAR API
        self.label10=ttk.Label(self.labelframe1, text="Titular:")
        self.label10.grid(column=0, row=10, padx=4, pady=4)
        self.api_titular=tk.StringVar()
        self.entryapi_titular=ttk.Entry(self.labelframe1, textvariable=self.api_titular, width=30, justify='center')
        self.entryapi_titular.config(state='disabled')
        self.entryapi_titular.grid(column=1, row=10, padx=4, pady=4)

        # BOTON CONSULTAR API
        self.boton2=ttk.Button(self.labelframe1, text="Cargar Datos", command=self.consulta_api)
        self.boton2.grid(column=1, row=11, padx=4, pady=4)
        # BOTON LIMPIAR CAMPOS
        self.boton3=ttk.Button(self.labelframe1, text="Limpiar Datos", command=self.limpiar_datos_1)
        self.boton3.grid(column=0, row=11, padx=4, pady=4)

    def consulta_api(self):
        if self.api_cliente.get()=="":
            mb.showerror("Cuidado","Necesitas colocar el ID del cliente primero.")
        else:
            # CONEXION ID UNO
            auth_data = {"IdCliente":self.api_cliente.get(),"Token":"77D5BDD4-1FEE-4A47-86A0-1E7D19EE1C74"}
            r = requests.post('http://192.168.20.44/ServiciosClubAlpha/api/Pagos/GetPedidoByCliente', data=auth_data)
            resp = r.json()
            # CONEXION ID DOS
            auth_data_dos = {"Token":"77D5BDD4-1FEE-4A47-86A0-1E7D19EE1C74"}
            r_dos = requests.get('http://192.168.20.44/ServiciosClubAlpha/api/Miembro/'+self.api_cliente.get(), data=auth_data_dos)
            resp_dos = r_dos.json()
            importe_total_api = sum(d['Importe'] for d in resp['Detalle'] if d)
            # TITULAR
            self.api_titular.set(f"{resp_dos['Nombre']}") # TITULAR
            self.api_membresia.set(f"{resp_dos['NoMembresia']}") # MEMBRESIA
            # DATOS
            self.api_pedido.set(f"{resp['NoPedido']}") # N° DE PEDIDO
            # OPERACION
            api_import_2 = (float(importe_total_api)) # IMPORTE CONEKTA
            api_import = importe_total_api   # IMPORTE
            # DATOS
            self.api_importe_2.set(api_import_2*100) # IMPORTE
            self.api_importe.set('{0:.2f}'.format(float(api_import))) # IMPORTE
            self.api_ov.set(f"{resp['Detalle'][0]['IDOrdendeVenta']}") 
            self.api_ovd.set(f"{resp['Detalle'][0]['IDOrdendeVentaDetalle']}")
            self.api_correo.set(f"{resp['CorreoCliente']}") # CORREO CLIENTE
            self.api_concepto.set(f"{resp['Detalle'][0]['Concepto']}") # CONCEPTO
            # CARGA DE DATOS
            api_datos = (self.api_cliente.get(), self.api_pedido.get(), self.api_importe.get(), self.api_ov.get(), self.api_ovd.get(),
                            self.api_correo.get(),self.api_concepto.get(), self.api_importe_2.get(), self.fechacarga.get(), self.api_titular.get(), self.api_membresia.get())
            self.articulo1.alta(api_datos)
            mb.showinfo("Información","Datos Cargados")
            mb.showinfo("Información","Continua con el PASO 2")

    def limpiar_datos_1(self):
        respuesta=mb.askyesno("Cuidado", "Limpiar los datos en Pantalla")
        if respuesta==True:
            self.fechacarga.set(value=fecha)
            self.api_cliente.set('')
            self.api_pedido.set('')
            self.api_importe.set('')
            self.api_ov.set('')
            self.api_ovd.set('')
            self.api_correo.set('')
            self.api_concepto.set('')
            self.api_titular.set('')

    # PAGINA 2
    def carga_conekta(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="PASO 2")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Crear Referencia de pago al Cliente")
        self.labelframe2.grid(column=0, row=0, padx=255, pady=10)
        # FECHA DE CREACION
        self.label10=ttk.Label(self.labelframe2, text="Fecha de Carga:")
        self.label10.grid(column=0, row=1, padx=4, pady=4)
        self.carga_fechacarga=tk.StringVar()
        self.entrycarga_fechacarga=ttk.Entry(self.labelframe2, textvariable=self.carga_fechacarga, width=30, justify='center')
        self.entrycarga_fechacarga.config(state='disabled')
        self.entrycarga_fechacarga.grid(column=1, row=1, padx=4, pady=4)
        # ID CLIENTE API
        self.label11=ttk.Label(self.labelframe2, text="ID CLIENTE:")
        self.label11.grid(column=0, row=2, padx=4, pady=4)
        self.carga_api_cliente=tk.StringVar()
        self.entrycarga_api_cliente=ttk.Entry(self.labelframe2, textvariable=self.carga_api_cliente, width=30, justify='center')
        self.entrycarga_api_cliente.config(state='disabled')
        self.entrycarga_api_cliente.grid(column=1, row=2, padx=4, pady=4)
        # N° DE PEDIDO API
        self.label12=ttk.Label(self.labelframe2, text="N° de Pedido:")
        self.label12.grid(column=0, row=3, padx=4, pady=4)
        self.carga_api_pedido=tk.StringVar()
        self.entrycarga_api_pedido=ttk.Entry(self.labelframe2, textvariable=self.carga_api_pedido, width=30, justify='center')
        self.entrycarga_api_pedido.config(state='disabled')
        self.entrycarga_api_pedido.grid(column=1, row=3, padx=4, pady=4)
        # IMPORTE API
        self.label13=ttk.Label(self.labelframe2, text="Importe:")
        self.label13.grid(column=0, row=4, padx=4, pady=4)
        self.carga_api_importe=tk.StringVar()
        self.entrycarga_api_importe=ttk.Entry(self.labelframe2, textvariable=self.carga_api_importe, width=30, justify='center')
        self.entrycarga_api_importe.config(state='disabled')
        self.entrycarga_api_importe.grid(column=1, row=4, padx=4, pady=4)
        # IMPORTE 2 API
        self.label14=ttk.Label(self.labelframe2, text="Importe:")
        #self.label14.grid(column=0, row=5, padx=4, pady=4)
        self.carga_api_importe_2=tk.StringVar()
        self.entrycarga_api_importe_2=ttk.Entry(self.labelframe2, textvariable=self.carga_api_importe_2, width=30, justify='center')
        self.entrycarga_api_importe_2.config(state='disabled')
        #self.entrycarga_api_importe_2.grid(column=1, row=5, padx=4, pady=4)
        # ORDEN DE VENTA API
        self.label15=ttk.Label(self.labelframe2, text="Orden de Venta:")
        self.label15.grid(column=0, row=6, padx=4, pady=4)
        self.carga_api_ov=tk.StringVar()
        self.entrycarga_api_ov=ttk.Entry(self.labelframe2, textvariable=self.carga_api_ov, width=30, justify='center')
        self.entrycarga_api_ov.config(state='disabled')
        self.entrycarga_api_ov.grid(column=1, row=6, padx=4, pady=4)
        # ORDEN DE VENTA DETALLE API
        self.label16=ttk.Label(self.labelframe2, text="Orden de Venta Detalle:")
        self.label16.grid(column=0, row=7, padx=4, pady=4)
        self.carga_api_ovd=tk.StringVar()
        self.entrycarga_api_ovd=ttk.Entry(self.labelframe2, textvariable=self.carga_api_ovd, width=30, justify='center')
        self.entrycarga_api_ovd.config(state='disabled')
        self.entrycarga_api_ovd.grid(column=1, row=7, padx=4, pady=4)
        # CORREO ELECTRONICO API
        self.label17=ttk.Label(self.labelframe2, text="Correo Cliente:")
        self.label17.grid(column=0, row=8, padx=4, pady=4)
        self.carga_api_correo=tk.StringVar()
        self.entrycarga_api_correo=ttk.Entry(self.labelframe2, textvariable=self.carga_api_correo, width=30, justify='center')
        self.entrycarga_api_correo.config(state='disabled')
        self.entrycarga_api_correo.grid(column=1, row=8, padx=4, pady=4)
        # CONCEPTO API
        self.label18=ttk.Label(self.labelframe2, text="Concepto:")
        self.label18.grid(column=0, row=9, padx=4, pady=4)
        self.carga_api_concepto=tk.StringVar()
        self.entrycarga_api_concepto=ttk.Entry(self.labelframe2, textvariable=self.carga_api_concepto, width=30, justify='center')
        self.entrycarga_api_concepto.config(state='disabled')
        self.entrycarga_api_concepto.grid(column=1, row=9, padx=4, pady=4)
        # CARGA DATOS API
        self.label19=ttk.Label(self.labelframe2, text="Carga Datos:")
        #self.label19.grid(column=0, row=9, padx=4, pady=4)
        self.carga_datos_api_1=tk.StringVar(value="1")
        self.entrycarga_datos_api_1=ttk.Entry(self.labelframe2, textvariable=self.carga_datos_api_1, width=30, justify='center')
        self.entrycarga_datos_api_1.config(state='disabled')
        #self.entrycarga_datos_api_1.grid(column=1, row=9, padx=4, pady=4)
        # TITULAR
        self.label21=ttk.Label(self.labelframe2, text="Titular:")
        self.label21.grid(column=0, row=11, padx=4, pady=4)
        self.carga_api_titular=tk.StringVar()
        self.entrycarga_api_titular=ttk.Entry(self.labelframe2, textvariable=self.carga_api_titular, width=30, justify='center')
        self.entrycarga_api_titular.config(state='disabled')
        self.entrycarga_api_titular.grid(column=1, row=11, padx=4, pady=4)
        # FECHA LIMITE
        self.label22=ttk.Label(self.labelframe2, text="Dias para Pagar:")
        self.label22.grid(column=0, row=10, padx=4, pady=4)
        self.dias_pago=tk.StringVar()
        self.monthchoosen = ttk.Combobox(self.labelframe2, width = 27, textvariable = self.dias_pago, justify='center', state="readonly")
        self.monthchoosen['values'] = ('1', '2', '3', '4', '5')
        self.monthchoosen.grid(column = 1, row = 10)
        # MEMBRESIA
        self.label21=ttk.Label(self.labelframe2, text="Membresia:")
        self.carga_api_membresia=tk.StringVar()
        self.entrycarga_api_membresia=ttk.Entry(self.labelframe2, textvariable=self.carga_api_membresia, width=30, justify='center')
        self.entrycarga_api_membresia.config(state='disabled')

        # BOTON CARGAR
        self.boton_mail=ttk.Button(self.labelframe2, text="Cargar Datos", command=self.cargar_datos_api)
        self.boton_mail.grid(column=0, row=12, padx=4, pady=4)
        # BOTON ENVIAR CORREO
        self.boton_mail_send=ttk.Button(self.labelframe2, text="Procesar Orden", command=self.send_conekta)
        self.boton_mail_send.grid(column=1, row=12, padx=4, pady=4)
        # BOTON LIMPIAR CAMPOS
        self.boton3=ttk.Button(self.labelframe2, text="Limpiar Datos", command=self.limpiar_datos_2)
        self.boton3.grid(column=2, row=12, padx=4, pady=4)

    def cargar_datos_api(self):
        carga_datos_api =(self.carga_datos_api_1.get(), )
        respuesta_mail=self.articulo1.consulta(carga_datos_api)
        if len(respuesta_mail)>0:
            self.carga_fechacarga.set(respuesta_mail[0][0])
            self.carga_api_cliente.set(respuesta_mail[0][1])
            self.carga_api_pedido.set(respuesta_mail[0][2])
            self.carga_api_importe.set(respuesta_mail[0][3])
            self.carga_api_importe_2.set(respuesta_mail[0][4])
            self.carga_api_ov.set(respuesta_mail[0][5])
            self.carga_api_ovd.set(respuesta_mail[0][6])
            self.carga_api_correo.set(respuesta_mail[0][7])
            self.carga_api_concepto.set(respuesta_mail[0][8])
            self.carga_api_titular.set(respuesta_mail[0][9])
            self.carga_api_membresia.set(respuesta_mail[0][10])
        else:
            self.carga_fechacarga.set('')
            self.carga_api_cliente.set('')
            self.carga_api_pedido.set('')
            self.carga_api_importe.set('')
            self.carga_api_importe_2.set('')
            self.carga_api_ov.set('')
            self.carga_api_ovd.set('')
            self.carga_api_correo.set('')
            self.carga_api_concepto.set('')
            self.carga_api_titular.set('')
            self.carga_api_membresia.set('')
            mb.showinfo("Información", "No existe un cliente\n Error al cargar el paso 1")

    def send_conekta(self):
        if self.carga_api_cliente.get()=="" or self.dias_pago.get()=="":
            mb.showerror("Cuidado","Necesitas Cargar los Datos primero.")
        else:
            dias_pago_oxxo = int(self.dias_pago.get())
            thirty_days_from_now = int((datetime.now() + timedelta(days=dias_pago_oxxo)).timestamp())
            # ENVIO A CONEKTA
            order = conekta.Order.create({
                "line_items": [{
                "name": "Pago Oxxo Club Alpha",
                "unit_price": self.carga_api_importe_2.get(), # MONTO A PAGAR
                "sku": "Pago en Oxxo",
                "quantity": 1
                }],
                "shipping_lines": [{
                    "amount": 0,
                    "carrier": "Club Alpha",
                    "method": "Pago Oxxo Pay"
                }],
                "currency": "MXN",
                "customer_info": {
                    "name": self.carga_api_titular.get(),
                    "email": self.carga_api_correo.get(),
                    "phone": "+5218181818181"
                },
                "shipping_contact":{
                    "address": {
                        "street1": "Blvd. Valsequillo 903, Prados Agua Azul",
                        "postal_code": "72430",
                        "state": "Puebla",
                        "country": "MX"
                    }
                },
                "charges":[{
                    "payment_method": {
                        "type": "oxxo_cash",
                        "expires_at": thirty_days_from_now
                    }
                }],
                "metadata": 
                    {
                        "NoPedido": self.carga_api_pedido.get(),
                        "Monto": self.carga_api_importe.get(),
                        "Notarjeta": "",
                        "FolioInterbancario": "",
                        "NoAutorizacion": "",
                        "FechaPago": "",
                        "HoraPago": "",
                        "TitularCuenta": self.carga_api_titular.get(),
                        "IDCliente": self.carga_api_cliente.get(),
                        "Membresia": self.carga_api_membresia.get()
                    }
            })
            order = order
            # MENSAJE EXITO
            #mb.showinfo("Información", "Los datos fueron enviados correctamente.\n"+ "\nID: " + order.id + "\nReferencia: " 
            #+ order.charges[0].payment_method.reference + "\nMonto: " + str(order.amount/100) + order.currency)
            # SAVE DATOS CONEKTA
            datos_conekta = (order.id, order.charges[0].payment_method.service_name, order.charges[0].payment_method.reference, str(order.amount/100), order.currency)
            self.articulo1.referencias(datos_conekta)
            #mb.showinfo("Información","Continua con el PASO 3")
            # ENVIO DE CONEKTA
            monto_oxxo = ('{:.2f}'.format(float(self.carga_api_importe.get())))
            #monto_oxxo = self.monto_mail.get()
            email_content = """
            <html>
                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                    <title>Referencia de Pago</title>
                    <style type="text/css">
                        /* Reset -------------------------------------------------------------------- */
                        * 	 { margin: 0;padding: 0; }
                        body { font-size: 14px; }

                        /* OPPS --------------------------------------------------------------------- */

                        h3 {
                            margin-bottom: 10px;
                            font-size: 15px;
                            font-weight: 600;
                            text-transform: uppercase;
                        }

                        .opps {
                            width: 496px; 
                            border-radius: 4px;
                            box-sizing: border-box;
                            padding: 0 45px;
                            margin: 40px auto;
                            overflow: hidden;
                            border: 1px solid #b0afb5;
                            font-family: 'Open Sans', sans-serif;
                            color: #4f5365;
                        }

                        .opps-reminder {
                            position: relative;
                            top: -1px;
                            padding: 9px 0 10px;
                            font-size: 11px;
                            text-transform: uppercase;
                            text-align: center;
                            color: #ffffff;
                            background: #000000;
                        }

                        .opps-info {
                            margin-top: 26px;
                            position: relative;
                        }

                        .opps-info:after {
                            visibility: hidden;
                            display: block;
                            font-size: 0;
                            content: " ";
                            clear: both;
                            height: 0;

                        }

                        .opps-brand {
                            width: 45%;
                            float: left;
                        }

                        .opps-brand img {
                            max-width: 150px;
                            margin-top: 2px;
                        }

                        .opps-ammount {
                            width: 55%;
                            float: right;
                        }

                        .opps-ammount h2 {
                            font-size: 36px;
                            color: #000000;
                            line-height: 24px;
                            margin-bottom: 15px;
                        }

                        .opps-ammount h2 sup {
                            font-size: 16px;
                            position: relative;
                            top: -2px
                        }

                        .opps-ammount p {
                            font-size: 10px;
                            line-height: 14px;
                        }

                        .opps-reference {
                            margin-top: 14px;
                        }

                        h1 {
                            font-size: 27px;
                            color: #000000;
                            text-align: center;
                            margin-top: -1px;
                            padding: 6px 0 7px;
                            border: 1px solid #b0afb5;
                            border-radius: 4px;
                            background: #f8f9fa;
                        }

                        .opps-instructions {
                            margin: 32px -45px 0;
                            padding: 32px 45px 45px;
                            border-top: 1px solid #b0afb5;
                            background: #f8f9fa;
                        }

                        ol {
                            margin: 17px 0 0 16px;
                        }

                        li + li {
                            margin-top: 10px;
                            color: #000000;
                        }

                        a {
                            color: #1155cc;
                        }

                        .opps-footnote {
                            margin-top: 22px;
                            padding: 22px 20 24px;
                            color: #108f30;
                            text-align: center;
                            border: 1px solid #108f30;
                            border-radius: 4px;
                            background: #ffffff;
                        }
                    </style>
                    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,600,700" rel="stylesheet">
                </head>
                <body>
                    <div class="opps">
                        <div class="opps-header">
                            <div class="opps-reminder">Ficha digital. No es necesario imprimir.</div>
                            <div class="opps-info">
                                <div class="opps-brand"><img src="https://github.com/conekta-examples/oxxopay-payment-stub/blob/master/demo/oxxopay_brand.png?raw=true" alt="OXXOPay"></div>
                                <div class="opps-ammount">
                                    <h3>Monto a pagar</h3>
                                    <h2>$ """+monto_oxxo+""" <sup>MXN</sup></h2>
                                    <p>OXXO cobrara una comision adicional al momento de realizar el pago.</p>
                                </div>
                            </div><br><br><br><br>
                            <div class="opps-reference">
                                <h3>Referencia</h3>
                                <h1>"""+order.charges[0].payment_method.reference+"""</h1> 
                            </div><br>
                        </div>
                        <div class="opps-instructions">
                            <h3>Instrucciones</h3>
                            <ol>
                                <li>Acude a la tienda OXXO mas cercana. <a href="https://www.google.com.mx/maps/search/oxxo/" target="_blank">Encuentrala aqui</a>.</li>
                                <li>Indica en caja que quieres realizar un pago de <strong>OXXOPay</strong>.</li>
                                <li>Dicta al cajero el numero de referencia en esta ficha para que ingrese directamete en la pantalla de venta.</li>
                                <li>Realiza el pago correspondiente con dinero en efectivo.</li>
                                <li>Al confirmar tu pago, el cajero te entregara un comprobante impreso. <strong>En el podras verificar que se haya realizado correctamente.</strong> Conserva este comprobante de pago.</li>
                            </ol>
                            <div class="opps-footnote"><img src="https://www.clubalpha.com.mx/images/logo_positivo2.png" alt="OXXOPay" ></div>
                        </div>
                    </div>
                </body>
            </html>
            """
            msg = email.message.Message()
            msg['Subject'] = "Club Alpha - Referencia de pago para "+self.carga_api_titular.get()
            msg['From'] = 'notificaciones@clubalpha.com.mx'
            msg['To'] = self.carga_api_correo.get() # CLIENTE
            password = "6Respugu"
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)
            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string())
            mb.showinfo("Información", "El Correo y la Referencia fue enviada con exito.")
            mb.showinfo("Información","Referencia de Pago Oxxo Completada")
        
    def limpiar_datos_2(self):
        respuesta=mb.askyesno("Cuidado", "Limpiar los datos en Pantalla")
        if respuesta==True:
            # LIMPIA INPUT
            self.carga_fechacarga.set('')
            self.carga_api_cliente.set('')
            self.carga_api_pedido.set('')
            self.carga_api_importe.set('')
            self.carga_api_importe_2.set('')
            self.carga_api_ov.set('')
            self.carga_api_ovd.set('')
            self.carga_api_correo.set('')
            self.carga_api_concepto.set('')
            self.carga_api_pedido.set('')
            self.dias_pago.set('')
            self.carga_api_titular.set('')

    # PAGINA 3
    def enviar_correo_cliente(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="PASO 3")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Enviar Referencia de Pago")
        self.labelframe3.grid(column=0, row=0, padx=255, pady=10)
        # VALIDACION
        self.label22=ttk.Label(self.labelframe3, text="Validacion:")
        self.mail_validacion=tk.StringVar(value="1")
        self.entrymail_validacion=ttk.Entry(self.labelframe3, textvariable=self.mail_validacion)
        # FECHA DE CREACION
        self.label22=ttk.Label(self.labelframe3, text="Fecha de Carga:")
        self.label22.grid(column=0, row=1, padx=4, pady=4)
        self.mail_fechacarga=tk.StringVar()
        self.entrymail_fechacarga=ttk.Entry(self.labelframe3, textvariable=self.mail_fechacarga, width=30, justify='center')
        self.entrymail_fechacarga.config(state='disabled')
        self.entrymail_fechacarga.grid(column=1, row=1, padx=4, pady=4)
        # ID CLIENTE API
        self.label23=ttk.Label(self.labelframe3, text="ID CLIENTE:")
        self.label23.grid(column=0, row=2, padx=4, pady=4)
        self.mail_api_cliente=tk.StringVar()
        self.entrymail_api_cliente=ttk.Entry(self.labelframe3, textvariable=self.mail_api_cliente, width=30, justify='center')
        self.entrymail_api_cliente.config(state='disabled')
        self.entrymail_api_cliente.grid(column=1, row=2, padx=4, pady=4)
        # IMPORTE API
        self.label25=ttk.Label(self.labelframe3, text="Importe:")
        self.label25.grid(column=0, row=4, padx=4, pady=4)
        self.mail_api_importe=tk.StringVar()
        self.entrymail_api_importe=ttk.Entry(self.labelframe3, textvariable=self.mail_api_importe, width=30, justify='center')
        self.entrymail_api_importe.config(state='disabled')
        self.entrymail_api_importe.grid(column=1, row=4, padx=4, pady=4)
        # IMPORTE 2 API
        self.label26=ttk.Label(self.labelframe3, text="Importe:")
        #self.label26.grid(column=0, row=5, padx=4, pady=4)
        self.mail_api_importe_2=tk.StringVar()
        self.entrymail_api_importe_2=ttk.Entry(self.labelframe3, textvariable=self.mail_api_importe_2, width=30, justify='center')
        self.entrymail_api_importe_2.config(state='disabled')
        #self.entrymail_api_importe_2.grid(column=1, row=5, padx=4, pady=4)
        # CORREO ELECTRONICO API
        self.label29=ttk.Label(self.labelframe3, text="Correo Cliente:")
        self.label29.grid(column=0, row=8, padx=4, pady=4)
        self.mail_api_correo=tk.StringVar()
        self.entrymail_api_correo=ttk.Entry(self.labelframe3, textvariable=self.mail_api_correo, width=30, justify='center')
        self.entrymail_api_correo.config(state='disabled')
        self.entrymail_api_correo.grid(column=1, row=8, padx=4, pady=4)
        # TITULAR
        self.label31=ttk.Label(self.labelframe3, text="Titular:")
        self.label31.grid(column=0, row=11, padx=4, pady=4)
        self.mail_api_titular=tk.StringVar()
        self.entrymail_api_titular=ttk.Entry(self.labelframe3, textvariable=self.mail_api_titular, width=30, justify='center')
        self.entrymail_api_titular.config(state='disabled')
        self.entrymail_api_titular.grid(column=1, row=11, padx=4, pady=4)
        # REFERENCIA OXXO
        self.label32=ttk.Label(self.labelframe3, text="Referencia:")
        self.label32.grid(column=0, row=12, padx=4, pady=4)
        self.mail_api_ref=tk.StringVar()
        self.entrymail_api_ref=ttk.Entry(self.labelframe3, textvariable=self.mail_api_ref, width=30, justify='center')
        self.entrymail_api_ref.config(state='disabled')
        self.entrymail_api_ref.grid(column=1, row=12, padx=4, pady=4)

        # BOTON CARGAR
        self.boton_mail_carga=ttk.Button(self.labelframe3, text="Cargar Datos", command=self.cargar_datos_db)
        self.boton_mail_carga.grid(column=0, row=13, padx=4, pady=4)
        # BOTON ENVIAR CORREO
        self.boton_mail_envio=ttk.Button(self.labelframe3, text="Enviar Correo", command=self.enviar_correo)
        self.boton_mail_envio.grid(column=1, row=13, padx=4, pady=4)
        # BOTON LIMPIAR DATOS
        self.boton_3=ttk.Button(self.labelframe3, text="Limpiar Datos", command=self.limpiar_datos_3)
        self.boton_3.grid(column=2, row=13, padx=4, pady=4)

    def cargar_datos_db(self):
        carga_datos_db = (self.mail_validacion.get(), )
        respuesta_mail=self.articulo1.consulta_mail(carga_datos_db)
        if len(respuesta_mail)>0:
            self.mail_fechacarga.set(respuesta_mail[0][0])
            self.mail_api_cliente.set(respuesta_mail[0][1])
            self.mail_api_importe.set(respuesta_mail[0][2])
            self.mail_api_importe_2.set(respuesta_mail[0][3])
            self.mail_api_correo.set(respuesta_mail[0][4])
            self.mail_api_titular.set(respuesta_mail[0][5])
            self.mail_api_ref.set(respuesta_mail[0][6])
        else:
            self.mail_fechacarga.set('')
            self.mail_api_cliente.set('')
            self.mail_api_importe.set('')
            self.mail_api_importe_2.set('')
            self.mail_api_correo.set('')
            self.mail_api_titular.set('')
            self.mail_api_ref.set('')
            mb.showinfo("Información", "No existe un cliente\n Error al cargar el paso 1")

    def enviar_correo(self):
        if self.mail_api_importe.get()=="" or self.mail_api_titular.get()=="":
            mb.showerror("Cuidado","Necesitas Cargar los Datos primero.")
        else:
            monto_oxxo = ('{:.2f}'.format(float(self.mail_api_importe.get())))
            #monto_oxxo = self.monto_mail.get()
            email_content = """
            <html>
                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                    <title>Referencia de Pago</title>
                    <style type="text/css">
                        /* Reset -------------------------------------------------------------------- */
                        * 	 { margin: 0;padding: 0; }
                        body { font-size: 14px; }

                        /* OPPS --------------------------------------------------------------------- */

                        h3 {
                            margin-bottom: 10px;
                            font-size: 15px;
                            font-weight: 600;
                            text-transform: uppercase;
                        }

                        .opps {
                            width: 496px; 
                            border-radius: 4px;
                            box-sizing: border-box;
                            padding: 0 45px;
                            margin: 40px auto;
                            overflow: hidden;
                            border: 1px solid #b0afb5;
                            font-family: 'Open Sans', sans-serif;
                            color: #4f5365;
                        }

                        .opps-reminder {
                            position: relative;
                            top: -1px;
                            padding: 9px 0 10px;
                            font-size: 11px;
                            text-transform: uppercase;
                            text-align: center;
                            color: #ffffff;
                            background: #000000;
                        }

                        .opps-info {
                            margin-top: 26px;
                            position: relative;
                        }

                        .opps-info:after {
                            visibility: hidden;
                            display: block;
                            font-size: 0;
                            content: " ";
                            clear: both;
                            height: 0;

                        }

                        .opps-brand {
                            width: 45%;
                            float: left;
                        }

                        .opps-brand img {
                            max-width: 150px;
                            margin-top: 2px;
                        }

                        .opps-ammount {
                            width: 55%;
                            float: right;
                        }

                        .opps-ammount h2 {
                            font-size: 36px;
                            color: #000000;
                            line-height: 24px;
                            margin-bottom: 15px;
                        }

                        .opps-ammount h2 sup {
                            font-size: 16px;
                            position: relative;
                            top: -2px
                        }

                        .opps-ammount p {
                            font-size: 10px;
                            line-height: 14px;
                        }

                        .opps-reference {
                            margin-top: 14px;
                        }

                        h1 {
                            font-size: 27px;
                            color: #000000;
                            text-align: center;
                            margin-top: -1px;
                            padding: 6px 0 7px;
                            border: 1px solid #b0afb5;
                            border-radius: 4px;
                            background: #f8f9fa;
                        }

                        .opps-instructions {
                            margin: 32px -45px 0;
                            padding: 32px 45px 45px;
                            border-top: 1px solid #b0afb5;
                            background: #f8f9fa;
                        }

                        ol {
                            margin: 17px 0 0 16px;
                        }

                        li + li {
                            margin-top: 10px;
                            color: #000000;
                        }

                        a {
                            color: #1155cc;
                        }

                        .opps-footnote {
                            margin-top: 22px;
                            padding: 22px 20 24px;
                            color: #108f30;
                            text-align: center;
                            border: 1px solid #108f30;
                            border-radius: 4px;
                            background: #ffffff;
                        }
                    </style>
                    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,600,700" rel="stylesheet">
                </head>
                <body>
                    <div class="opps">
                        <div class="opps-header">
                            <div class="opps-reminder">Ficha digital. No es necesario imprimir.</div>
                            <div class="opps-info">
                                <div class="opps-brand"><img src="https://github.com/conekta-examples/oxxopay-payment-stub/blob/master/demo/oxxopay_brand.png?raw=true" alt="OXXOPay"></div>
                                <div class="opps-ammount">
                                    <h3>Monto a pagar</h3>
                                    <h2>$ """+monto_oxxo+""" <sup>MXN</sup></h2>
                                    <p>OXXO cobrara una comision adicional al momento de realizar el pago.</p>
                                </div>
                            </div><br><br><br><br>
                            <div class="opps-reference">
                                <h3>Referencia</h3>
                                <h1>"""+self.mail_api_ref.get()+"""</h1> 
                            </div><br>
                        </div>
                        <div class="opps-instructions">
                            <h3>Instrucciones</h3>
                            <ol>
                                <li>Acude a la tienda OXXO mas cercana. <a href="https://www.google.com.mx/maps/search/oxxo/" target="_blank">Encuentrala aqui</a>.</li>
                                <li>Indica en caja que quieres realizar un pago de <strong>OXXOPay</strong>.</li>
                                <li>Dicta al cajero el numero de referencia en esta ficha para que ingrese directamete en la pantalla de venta.</li>
                                <li>Realiza el pago correspondiente con dinero en efectivo.</li>
                                <li>Al confirmar tu pago, el cajero te entregara un comprobante impreso. <strong>En el podras verificar que se haya realizado correctamente.</strong> Conserva este comprobante de pago.</li>
                            </ol>
                            <div class="opps-footnote"><img src="https://www.clubalpha.com.mx/images/logo_positivo2.png" alt="OXXOPay" ></div>
                        </div>
                    </div>
                </body>
            </html>
            """
            msg = email.message.Message()
            msg['Subject'] = "Club Alpha - Referencia de pago para "+self.mail_api_titular.get()
            msg['From'] = 'notificaciones@clubalpha.com.mx'
            msg['To'] = self.mail_api_correo.get() # CLIENTE
            password = "6Respugu"
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)
            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string())
            mb.showinfo("Información", "El correo fue enviado con exito.")
            mb.showinfo("Información","Referencia de Pago Oxxo Completada")

    def limpiar_datos_3(self):
        respuesta=mb.askyesno("Cuidado", "Limpiar los datos en Pantalla")
        if respuesta==True:
            self.mail_fechacarga.set('')
            self.mail_api_cliente.set('')
            self.mail_api_importe.set('')
            self.mail_api_importe_2.set('')
            self.mail_api_correo.set('')
            self.mail_api_titular.set('')
            self.mail_api_ref.set('')

aplicacion1=FormularioArticulos()
#El módulo 'articulos.py' contiene toda la lógica de acceso a SQLite.
