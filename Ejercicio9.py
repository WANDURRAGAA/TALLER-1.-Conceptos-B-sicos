opcion = input("¿Quieres una pizza vegetariana? (si o no): ")

if opcion.lower() == "si":
    print("Ingredientes disponibles: Pimiento y tofu")
else:
    print("Ingredientes disponibles: Peperoni, Jamón y Salmón")

ingrediente = input("Elija un ingrediente: ")

if opcion.lower() == "si":
    print("Pizza vegetariana con mozzarella, tomate, y", ingrediente)
else:
    print("Pizza no vegetariana con mozzarella, y", ingrediente)