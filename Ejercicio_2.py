nombre1 = input("Ingrese el nombre del primer usuario: ")
edad1 = int(input("Ingrese la edad del primer usuario: "))

nombre2 = input("Ingrese el nombre del segundo usuario: ")
edad2 = int(input("Ingrese la edad del segundo usuario: "))

if edad1 < edad2:
    nombre_menor = nombre1
elif edad2 < edad1:
    nombre_menor = nombre2
else:
    nombre_menor = "Ambos tienen la misma edad"

print("El menor es:", nombre_menor)