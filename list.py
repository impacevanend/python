demo_list = [1,"hello",3.14,True,[1,2,3]]

#print(demo_list[4][2])
colors = ["red","blue","green"]

#constructor mas dupla para obtener arreglo!

nuevaLista = list((1,2,3,4))

print(nuevaLista)

# lista por rango

r = list(range(1,10))
print(r)
#tipo de dato
print(type(colors))

#*Metodos y propiedades de listas

#print(dir(colors))

#*cantidad de elementos en una lista.
print(len(colors))
#imprimir en pantalla la posición de la lista
print(colors[2])
print(colors[-1])
#Validar si un elemento existe en una lista
print("green" in colors)

#Cambiar un elemento de la lista por otro.
print(f"El contenido actual es: {colors}")
colors[1] = "yellow"

print(f"El nuevo contenido es: {colors}")

#agregar nuevo elemento a la lista

colors.append("violet")
print(colors)

#agregar varios elementos a la lista, sirve con listas[] y tuplas()
colors.extend(("purple","brown","black"))
print(colors)

#colocar un elemento en un posición determinad

colors.insert(1,"orange")

print(colors)

colors.insert(-1,"orange")
print(colors)

#Insertar elemento en la última posición

colors.insert(len(colors),"pink")
print(colors)

#Quitar el último elemento de una lista

print(f"Los elementos actuales en la lista son:{colors}")

colors.pop()

print(f"Se elemino el último elemento, ahora la lista presenta:{colors}")


#Remover determinado elemento de la lista

print(colors)
colors.remove("yellow")
print(f"Los nuevos elementos son:{colors}")

# El método pop puede eliminar con indice.
print("--------------------------")
print(f"Se muestran los valores antes de eliminarlos con pop(), con el indice cero{colors}")
colors.pop(0)
print(f"Se elimino con pop el valor 'red'{colors}")
print("--------------------------")

