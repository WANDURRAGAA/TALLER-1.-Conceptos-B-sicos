import random
def adivina_n(nivel):

    numero_secreto = random.randint(1, 200)
    intentos = 0

    if nivel == "basico":
        print("nivel básico")
        while True:
            intento = int(input("Adivina el número: "))
            intentos += 1

            if intento == numero_secreto:
                print("Adivinaste el número en", intentos, "intentos.")
                break
            if intento < numero_secreto:
                print("El número es mayor.")
            else:
                print("El número es menor.")

    elif nivel == "experto":
        print("nivel experto")
        for _ in range(5):
            intento = int(input("Adivina el número: "))
            intentos += 1

            if intento == numero_secreto:
                print("Adivinaste el número en", intentos, "intentos.")
                return
            if intento < numero_secreto:
                print("El número es mayor.")
            else:
                print("El número es menor.")

        print("Perdiste tus 5 oportunidades. El número secreto era", numero_secreto)

    else:
        print("Error. Por favor, elige basico o experto.")

nivel_juego = input("Elige un nivel (basico/experto): ")
adivina_n(nivel_juego)