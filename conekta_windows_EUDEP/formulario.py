import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
 #CONEKTA
import conekta
conekta.api_key = "key_PJY8U2Lqss9ucyT6rVNfAQ"    # Clave Privada
#conekta.api_key = "key_Xd1qWTsdexemXbZ6yhvsrrw"  # Clave Publica
from datetime import datetime, timedelta
#thirty_days_from_now = int((datetime.now() + timedelta(days=1)).timestamp())
fecha = datetime.now()
import articulos
# CORREO
import smtplib
import email.message

opciones = {
            "Inscripción": ("200.00"), 
            "Inscripción Anticipo 50%": ("1000.00"),
            "Inscripción Finiquito": ("1000.00"), 
            "Reinscripción": ("2000.00"), 
            "Cuota SEP": ("120.00"), 
            "Colegiatura": ("4000.00"), 
            "Recursamiento de Materia": ("4000.00"), 
            "Mensualidad Alpha": ("350.00"), 
            "Constancia de Estudios": ("150.00"), 
            "Examen Extraordinario": ("180.00"), 
            "Legalización de Certificado": ("350.00"),
            "Otro Cargo": ("0")
        }

class FormularioArticulos:
    def manual(self):
        mb.showinfo("Manual para Operación", 
                    "PASO 1: \nCARGAR DATOS DEL CLIENTE.\n\nNecesitaras colocar correctamente el correo para que no tengas problemas al generar la orden.\nNo coloques doble punto en el Monto (00.00.0).\n\n"
                    "PASO 2: \nGENERAR REFERENCIA OXXO.\n\nAl dar Clic al boton Cargar Datos, el sistema cargara los datos anteriores, solo coloca los dias maximos para pagar.\n\n")

    def soporte(self):
        mb.showinfo("Información", "Correo de Soporte:\nivan.najera@clubalpha.com.mx")

    def salir(self):
       self.ventana1.destroy()

    def on_combobox_select(self, event):
        self.preciocarga.set("")
        self.preciocarga.config(values = opciones[self.tipo_pago.get()])

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
        self.crear_referencia_oxxo()
        #self.listado_completo()
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
        self.cuaderno1.add(self.pagina1, text="PASO 1 - Cargar Datos del Cliente")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Datos del Cliente")        
        self.labelframe1.grid(column=0, row=0, padx=220, pady=20)
        # NOMBRE CLIENTE
        self.label1=ttk.Label(self.labelframe1, text="Nombre Cliente:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga, width=33, justify='center')
        self.entrydescripcion.config(state='enabled')
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        # TELEFONO
        self.label3=ttk.Label(self.labelframe1, text="Telefono:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.telefonocarga=tk.StringVar(value="+52")
        self.entrytelefono=ttk.Entry(self.labelframe1, textvariable=self.telefonocarga, width=33, justify='center')
        self.entrytelefono.config(state='enabled')
        self.entrytelefono.grid(column=1, row=2, padx=4, pady=4)
        # CORREO
        self.label4=ttk.Label(self.labelframe1, text="Correo Electronico:")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.correocarga=tk.StringVar()
        self.entrycorreo=ttk.Entry(self.labelframe1, textvariable=self.correocarga, width=33, justify='center')
        self.entrycorreo.config(state='enabled')
        self.entrycorreo.grid(column=1, row=3, padx=4, pady=4)
        # DIRECCION
        self.label5=ttk.Label(self.labelframe1, text="Dirección:")
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.direccioncarga=tk.StringVar()
        self.entrydireccion=ttk.Entry(self.labelframe1, textvariable=self.direccioncarga, width=33, justify='center')
        self.entrydireccion.config(state='enabled')
        self.entrydireccion.grid(column=1, row=4, padx=4, pady=4)
        # TIPO DE PAGO
        self.label6=ttk.Label(self.labelframe1, text="Tipo de Pago:")
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.tipo_pago = ttk.Combobox(self.labelframe1, width="30", state="readonly", values=tuple(opciones.keys()))
        self.tipo_pago.grid(row="5", column="1")
        self.tipo_pago.bind("<<ComboboxSelected>>", self.on_combobox_select)
        # MONTO
        self.label7=ttk.Label(self.labelframe1, text="Monto:")
        self.label7.grid(column=0, row=6, padx=4, pady=4)
        self.preciocarga = ttk.Combobox(self.labelframe1, width="30")
        self.preciocarga.config(state='enabled')
        self.preciocarga.grid(row="6", column="1")
        # MONTO AJUSTADO
        self.label9=ttk.Label(self.labelframe1, text="Monto Ajustado:")
        #self.label9.grid(column=0, row=7, padx=4, pady=4)
        self.monto_ajustado=tk.StringVar()
        self.entrymonto_ajustado=ttk.Entry(self.labelframe1, textvariable=self.monto_ajustado, width=33, justify='center')
        self.entrymonto_ajustado.config(state='disabled')
        #self.entrymonto_ajustado.grid(column=1, row=7, padx=4, pady=4)
        # MONTO VISTA CLIENTE
        self.label9=ttk.Label(self.labelframe1, text="Monto Ajustado:")
        #self.label9.grid(column=0, row=8, padx=4, pady=4)
        self.monto_ajustado_vista=tk.StringVar()
        self.entrymonto_ajustado_vista=ttk.Entry(self.labelframe1, textvariable=self.monto_ajustado_vista, width=33, justify='center')
        self.entrymonto_ajustado_vista.config(state='disabled')
        #self.entrymonto_ajustado_vista.grid(column=1, row=8, padx=4, pady=4)
        # FECHA DE CREACION
        self.label8=ttk.Label(self.labelframe1, text="Fecha de Creación:")
        self.label8.grid(column=0, row=9, padx=4, pady=4)
        self.fechacarga=tk.StringVar(value=fecha)
        self.entryfecha=ttk.Entry(self.labelframe1, textvariable=self.fechacarga, width=33, justify='center')
        self.entryfecha.config(state='disabled')
        self.entryfecha.grid(column=1, row=9, padx=4, pady=4)
        # BOTON CONFIRMAR
        self.boton1=ttk.Button(self.labelframe1, text="Cargar Datos", command=self.cargar_datos_clientes)
        self.boton1.grid(column=1, row=10, padx=4, pady=4)
        # BOTON LIMPIAR
        self.boton2=ttk.Button(self.labelframe1, text="Limpiar Campos", command=self.limpiar_datos_1)
        self.boton2.grid(column=0, row=10, padx=4, pady=4)

    def cargar_datos_clientes(self):
        if self.preciocarga.get()=="" or self.descripcioncarga.get()=="":
            mb.showerror("Cuidado","Necesitas colocar totos los datos del cliente primero.")
        else:
            # OPERACION MONTO
            monto = (float(self.preciocarga.get())) # IMPORTE CONEKTA
            self.monto_ajustado.set(monto*100) # IMPORTE
            # CLIENTE VISTA MONTO
            monto_cliente_vista = self.preciocarga.get()
            self.monto_ajustado_vista.set(monto_cliente_vista)
            #self.monto_cliente.set('{0:.2f}'.format(float(monto_cliente_conversion))) # IMPORTE
            # GUARDA DATOS
            datos=(self.descripcioncarga.get(), self.telefonocarga.get(), self.correocarga.get(), self.direccioncarga.get(), self.tipo_pago.get(), self.monto_ajustado.get(), self.monto_ajustado_vista.get(), self.fechacarga.get())
            self.articulo1.alta(datos)
            # MENSAJE EXITO
            mb.showinfo("Información", "Los datos fueron cargados correctamente.")
            mb.showinfo("Información", "CONTINUA CON EL PASO 2.")

    def limpiar_datos_1(self):
        respuesta=mb.askyesno("Cuidado", "Limpiar los datos en Pantalla")
        if respuesta==True:
            self.descripcioncarga.set("")
            self.telefonocarga.set("")
            self.correocarga.set("")
            self.direccioncarga.set("")
            self.tipo_pago.set("")
            self.preciocarga.set("")
            self.monto_ajustado.set("")
    
    # PAGINA 2
    def crear_referencia_oxxo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="PASO 2 - Crear Referencia Oxxo")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Cargar Datos del Cliente")
        self.labelframe2.grid(column=0, row=0, padx=255, pady=10)
        # ID
        self.label1=ttk.Label(self.labelframe2, text="Validación:")
        #self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.id=tk.StringVar(value="1")
        self.entryid=ttk.Entry(self.labelframe2, textvariable=self.id, state="readonly", width=30, justify='center')
        #self.entryid.grid(column=1, row=0, padx=4, pady=4)
        # CLIENTE
        self.label2=ttk.Label(self.labelframe2, text="Cliente:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.cliente=tk.StringVar()
        self.entrycliente=ttk.Entry(self.labelframe2, textvariable=self.cliente, state="readonly", width=30, justify='center')
        self.entrycliente.grid(column=1, row=1, padx=4, pady=4)
        # TELEFONO
        self.label3=ttk.Label(self.labelframe2, text="Telefono:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.telefono=tk.StringVar()
        self.entrytelefono=ttk.Entry(self.labelframe2, textvariable=self.telefono, state="readonly", width=30, justify='center')
        self.entrytelefono.grid(column=1, row=2, padx=4, pady=4)
        # CORREO
        self.label4=ttk.Label(self.labelframe2, text="Correo:")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.correo=tk.StringVar()
        self.entrycorreo=ttk.Entry(self.labelframe2, textvariable=self.correo, state="readonly", width=30, justify='center')
        self.entrycorreo.grid(column=1, row=3, padx=4, pady=4)
        # DIRECCION
        self.label5=ttk.Label(self.labelframe2, text="Direccion:")
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.direccion=tk.StringVar()
        self.entrydireccion=ttk.Entry(self.labelframe2, textvariable=self.direccion, state="readonly", width=30, justify='center')
        self.entrydireccion.grid(column=1, row=4, padx=4, pady=4)
        # TIPO DE PAGO
        self.label6=ttk.Label(self.labelframe2, text="Tipo de Pago:")
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.tipo_pago_cons=tk.StringVar()
        self.entrytipo_pago_cons=ttk.Entry(self.labelframe2, textvariable=self.tipo_pago_cons, state="readonly", width=30, justify='center')
        self.entrytipo_pago_cons.grid(column=1, row=5, padx=4, pady=4)
        # MONTO
        self.label7=ttk.Label(self.labelframe2, text="Monto:")
        self.label7.grid(column=0, row=6, padx=4, pady=4)
        self.monto=tk.StringVar()
        self.entrymonto=ttk.Entry(self.labelframe2, textvariable=self.monto, state="readonly", width=30, justify='center')
        self.entrymonto.grid(column=1, row=6, padx=4, pady=4)
        # MONTO VISTA CLIENTE
        self.label8=ttk.Label(self.labelframe2, text="Monto:")
        self.label8.grid(column=0, row=7, padx=4, pady=4)
        self.monto_cliente=tk.StringVar()
        self.entrymonto_cliente=ttk.Entry(self.labelframe2, textvariable=self.monto_cliente, state="readonly", width=30, justify='center')
        self.entrymonto_cliente.grid(column=1, row=7, padx=4, pady=4)
        # FECHA LIMITE
        self.label22=ttk.Label(self.labelframe2, text="Dias para Pagar:")
        self.label22.grid(column=0, row=8, padx=4, pady=4)
        self.dias_pago=tk.StringVar()
        self.monthchoosen = ttk.Combobox(self.labelframe2, width = 27, textvariable = self.dias_pago, justify='center', state="readonly")
        self.monthchoosen['values'] = ('1', '2', '3', '4', '5')
        self.monthchoosen.grid(column = 1, row = 8)
        # FECHA DE CREACION
        self.label8=ttk.Label(self.labelframe2, text="Fecha Creacion:")
        self.label8.grid(column=0, row=9, padx=4, pady=4)
        self.fecha_creacion=tk.StringVar()
        self.entryfecha_creacion=ttk.Entry(self.labelframe2, textvariable=self.fecha_creacion, state="readonly", width=30, justify='center')
        self.entryfecha_creacion.grid(column=1, row=9, padx=4, pady=4)

        # BOTON CARGAR
        self.boton1=ttk.Button(self.labelframe2, text="Cargar Datos", command=self.cargar_datos_cliente_ref)
        self.boton1.grid(column=0, row=10, padx=4, pady=4)
        # BOTON REFERENCIA DE APGO
        self.boton2=ttk.Button(self.labelframe2, text="Crear Referencia", command=self.enviar_conekta)
        self.boton2.grid(column=1, row=10, padx=4, pady=4)
        # BOTON LIMPIAR DATOS
        self.boton3=ttk.Button(self.labelframe2, text="Limpiar Datos", command=self.limpiar_datos_2)
        self.boton3.grid(column=2, row=10, padx=4, pady=4)

    def cargar_datos_cliente_ref(self):
        datos=(self.id.get())
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.cliente.set(respuesta[0][0])
            self.telefono.set(respuesta[0][1])
            self.correo.set(respuesta[0][2])
            self.direccion.set(respuesta[0][3])
            self.tipo_pago_cons.set(respuesta[0][4])
            self.monto.set(respuesta[0][5]) # IMPORTE CONEKTA
            self.monto_cliente.set(respuesta[0][6])
            self.fecha_creacion.set(respuesta[0][7])
        else:
            self.cliente.set('')
            self.telefono.set('')
            self.correo.set('')
            self.direccion.set('')
            self.tipo_pago_cons.set('')
            self.monto.set('')
            self.monto_cliente.set('')
            self.fecha_creacion.set('')
            mb.showinfo("Información", "No existe un cliente con dicha referencia")

    def enviar_conekta(self):
        if self.correo.get()=="" or self.dias_pago.get()=="":
            mb.showerror("Cuidado","Necesitas Cargar los Datos primero.")
        else:
            dias_pago_oxxo = int(self.dias_pago.get())
            dias_para_pagar = int((datetime.now() + timedelta(days=dias_pago_oxxo)).timestamp())
            # ENVIO A CONEKTA
            order = conekta.Order.create({
                "line_items": [{
                "name": "Pago Oxxo EUDEP",
                "unit_price": self.monto.get(), # MONTO A PAGAR
                "sku": "Pago en Oxxo",
                "quantity": 1
                }],
                "shipping_lines": [{
                    "amount": 0,
                    "carrier": "EUDEP",
                    "method": "Pago Oxxo Pay"
                }],
                "currency": "MXN",
                "customer_info": {
                    "name": self.cliente.get(),
                    "email": self.correo.get(),
                    "phone": "+5218181818181"
                },
                "shipping_contact":{
                    "address": {
                        "street1": "Calle 36 Nte. 1830, Cristóbal Colon",
                        "postal_code": "72330",
                        "state": "Puebla",
                        "country": "MX"
                    }
                },
                "charges":[{
                    "payment_method": {
                        "type": "oxxo_cash",
                        "expires_at": dias_para_pagar
                    }
                }],
                "metadata": 
                    {
                        "Matricula": "",
                        "Monto": self.monto.get(),
                        "Carrera": "",
                        "ID": "",
                        "FechaPago": "",
                        "HoraPago": "",
                        "TitularCuenta": "",
                        "IDCliente": ""
                    }
            })
            order = order
            # SAVE DATOS CONEKTA
            datos_conekta = (order.id, order.charges[0].payment_method.service_name, order.charges[0].payment_method.reference, str(order.amount/100), order.currency)
            self.articulo1.referencias(datos_conekta)
            # ENVIO DE CONEKTA
            monto_oxxo = ('{:.2f}'.format(float(self.monto_cliente.get())))
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
                            <div class="opps-footnote"><img src="https://eudep.mx/wp-content/uploads/2021/03/logo-eudep-h-txt-bco.png" alt="OXXOPay" ></div>
                        </div>
                    </div>
                </body>
            </html>
            """
            msg = email.message.Message()
            msg['Subject'] = "EUDEP - Referencia de pago para "+self.cliente.get()
            msg['From'] = 'notificaciones@clubalpha.com.mx'
            msg['To'] = self.correo.get() # CLIENTE
            password = "6Respugu"
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)
            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string())
            mb.showinfo("Información", "El Correo y la Referencia fue enviada con exito.")
            mb.showinfo("Información","Referencia de Pago Oxxo Completada")

    def limpiar_datos_2(self):
        respuesta=mb.askyesno("Cuidado", "Limpiar los datos en Pantalla")
        if respuesta==True:
            self.cliente.set('')
            self.telefono.set('')
            self.correo.set('')
            self.direccion.set('')
            self.tipo_pago_cons.set('')
            self.monto.set('')
            self.monto_cliente.set('')
            self.fecha_creacion.set('')

    # PAGINA 3
    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Historico de Pagos")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Referencias de Pagos Generados")
        self.labelframe3.grid(column=0, row=0, padx=255, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Historico completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=40, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "Cliente: "+fila[0]+"\nTelefono: "+fila[1]+"\nCorreo: "+fila[2]+"\nDirección: "+fila[3]+"\nTipo de Pago: "
                                        +fila[4]+"\nMonto: "+str(fila[5])+"\nFecha: "+fila[6]+"\nID Orden: "+fila[7]+"\nReferencia Oxxo: "+fila[8]+"\n\n")


aplicacion1=FormularioArticulos()
#El módulo 'articulos.py' contiene toda la lógica de acceso a SQLite.
