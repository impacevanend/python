#Las tuplas son conjunto de datos, que no se pueden cambiar.

# x = (1,2,3)

# print(type(x))

moth = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")

#Constructor de tuplas

# y = tuple((1,2,3))

# print(y)

#*Conocer propiedades y métodos de una tupla.

#print(dir(y))

#*Una tupla debe contener mas de un elemento o colocar una coma a la izquierda del primer elemento.
w = (1)

print(type(w))#*Arroja un resultado de typo de dato entero.

z = (1,)

print(type(z))#*Arroja un resultado de typo de dato tupla.

#TODO MÉTODO DE UNA TUPLA

D = (1,2,3,4,5)

#Acceder a un elemento de la tupla.
print(D[0])

#TODO no se puede cambiar un elemento de la tupla por otro.

#*D[1] = 6

#TODO Eliminar toda la tupla

#*del D

# La tupla se utiliza en diccionarios o listas

locations = {
    (35.55, 39.80):"Tokyo",
    (35.55, 39.80):"New York",
}



