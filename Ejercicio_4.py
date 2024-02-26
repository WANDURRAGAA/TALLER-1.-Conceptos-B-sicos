def signo(valor):
    if valor > 0:
        print("El valor es positivo")
    elif valor < 0:
        print("El valor es negativo")
    else:
        print("El valor es cero")

valor = float(input("Ingrese un valor: "))
signo(valor)