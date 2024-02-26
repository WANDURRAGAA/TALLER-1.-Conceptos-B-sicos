def factura(precio_unitario, cantidad):
    iva = 0.16
    precio_bruto = precio_unitario * cantidad * (1 + iva)
    
    if precio_bruto > 500000:
        descuento = 0.15
        precio_bruto -= precio_bruto * descuento
    
    return precio_bruto

precio_unitario = float(input("Ingrese el precio del artículo: "))
cantidad = int(input("Ingrese la cantidad de unidades: "))

total_factura = factura(precio_unitario, cantidad)
print("El total de la factura es: ", total_factura)