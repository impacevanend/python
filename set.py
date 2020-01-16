#TODO Definición de un tipo de dato set: colección desordenada, no tiene un indice.

colors = {"Red","Green","Blue"}

print(type(colors))

#*Validar si un elemento esta en un conjunto de datos set.
print("Red" in colors)

#*Agregar un nuevo elemento al conjunto set

colors.add("Violet")

print(colors)

#todo imprime en pantalla -> {'Blue', 'Green', 'Violet', 'Red'}

#*Remover un elemento del conjunto set.

colors.remove("Red")
print(colors)

#*Remover todos los elementos de un conjunto set


colors.clear()
print(f"Resultado de utilizar el método clear():{colors}")
