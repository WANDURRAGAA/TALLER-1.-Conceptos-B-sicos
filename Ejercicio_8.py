# realiza un programa que si el peso de la mercancia es <= 500 kg la tarifa de envio es 40.000, si el peso de la mercancia es >500 kg AND <=750kg la tarifa de envio es 80.000, si el peso de la mercancia es >750 kg AND <=1000kg la tarifa de envio es 100.000, si el peso de la mercancia es >1000 kg la tarifa de envio es 500 por cada 10 kg adicionales. Descuentos: - Si el valor de la mercancía es >= a 300.000 y <= a 600.000 se hace un descuento del 20% sobre el valor del envío - Si el valor de la mercancía es > a 600.000 y <= a 1.000.000 se hace un descuento del 35% sobre el valor del envío - Si el valor de la mercancía es > a 1.000.000 se hace un descuento del 50% sobre el valor del envio. Promociones: - Si el pago se hace con tarjeta propia del almacén, no se cobra la tarifa de envío - Si paga en efectivo y el valor de la mercancía es superior a 500.000 no se cobra el envío. - Si paga en efectivo y el valor de la mercancía está entre 300.000 y 500.000 se hace un 50% de descuento sobre la tarifa de envío.


def ejercicio_8():
    peso = float(input("Ingrese el peso de la mercancia: "))
    valor = float(input("Ingrese el valor de la mercancia: "))
    pago = input("Ingrese la forma de pago: ")

    if peso <= 500:
        tarifa = 40000
    elif 500 < peso <= 750:
        tarifa = 80000
    elif 750 < peso <= 1000:
        tarifa = 100000
    elif peso > 1000:
        tarifa = 500 * (peso // 10)

    if 300000 <= valor <= 600000:
        descuento = tarifa * 0.20
    elif 600000 < valor <= 1000000:
        descuento = tarifa * 0.35
    elif valor > 1000000:
        descuento = tarifa * 0.50

    if pago == "tarjeta":
        tarifa = 0
    elif pago == "efectivo" and valor > 500000:
        tarifa = 0
    elif 300000 < valor < 500000:
        descuento = tarifa * 0.50

    print("El valor es: ", tarifa - descuento)
ejercicio_8()
