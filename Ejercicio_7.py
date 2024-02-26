def leer_numeros():
    num1 = int(input("primer número: "))
    num2 = int(input("segundo número: "))
    return num1, num2

def sumar_numeros():
    num1, num2 = leer_numeros()
    suma = num1 + num2
    print("La suma es:", suma)

def restar_numeros():
    num1, num2 = leer_numeros()
    if num1 >= num2:
        resta = num1 - num2
        print("La resta es:", resta)
    else:
        print("La operación no se puede realizar")

def multiplicar_numeros():
    num1, num2 = leer_numeros()
    if num1 != 0 and num2 != 0:
        multiplicacion = num1 * num2
        print("La multiplicación es:", multiplicacion)
    else:
        print("La operación no se pued realizar.")

def dividir_numeros():
    num1, num2 = leer_numeros()
    if num2 != 0:
        division = num1 / num2
        print("La división es:", division)
    else:
        print("La operación no se puedee realizar.")

def mostrar_menu():
    print("Menú:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")

mostrar_menu()
opcion = int(input("Seleccione: "))

while opcion != 5:
    if opcion == 1:
        sumar_numeros()
    elif opcion == 2:
        restar_numeros()
    elif opcion == 3:
        multiplicar_numeros()
    elif opcion == 4:
        dividir_numeros()
    else:
        print("Intenta de nuevo")

    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

print("bye")