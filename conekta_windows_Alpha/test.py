import requests, json
auth_data = {"IdCliente":60887,"Token":"77D5BDD4-1FEE-4A47-86A0-1E7D19EE1C74"}
r = requests.post('http://192.168.20.26/ServiciosClubAlpha/api/Pagos/GetPedidoByCliente', data=auth_data)
resp = r.json()
#print(f"IDCliente:{resp['IDCliente']}")
#print(f"{resp['IDCliente']}")
#print(f"{resp['NoPedido']}")
#print(f"{resp['Detalle'][0]['IDOrdendeVentaDetalle']}")

#for record in resp['Detalle']:
    #total = record.get('Importe')
    #list_total = total
    #test = sum(list_total)
    #print(list_total, end=" ")
    #print(list_total)

#print('{0:.2f}'.format(float(api_import)))

importe_total_api = sum(d['Importe'] for d in resp['Detalle'] if d)
print(importe_total_api)
print(float('%.3g'%importe_total_api))