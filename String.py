myStr = "Hello World"

#Consultar propiedades y metodos de String
#print(dir(myStr))

#String mayúsculas
print(myStr.upper())
#String minúscula
print(myStr.lower())
#String cambio de minúscula a mayúscula y viseversa
print(myStr.swapcase())
#String primera letra en mayúscula
print(myStr.capitalize())
#remplazar texto
print(myStr.replace("Hello","Bye"))
#remplazar texto convertir a mayúsculas, método encadenado.

print(myStr.replace("Hello","Bye").upper())
#Contar caracteres en una palabra
print(myStr.count("l"))
# Validar si un texto comienza con la palabra tal
print(myStr.startswith("hola"))
# Validar si un texto termina con la palabra tal
print(myStr.endswith("World"))
#dividir texto por espacio
#separa el texto por espacio(predeterminado), coma etc.
print(myStr.split())

#Buscar carácter, encuentra la posición.
print(myStr.find("o"))
#Buscar el indice del carácter
print(myStr.find("W"))
#Cantidad de caracteres
print(len(myStr))
#Buscar el indice de la palabra
print(myStr.index("e"))
#Conocer si el dato es numérico
print(myStr.isnumeric())
#Conocer si el dato es alfanumérico
print(myStr.isalpha())

#conocer el carácter en una posición
print(myStr[4])
print(myStr[-1])

#concatenar texto sin utilizar el signo +

print(f"Un saludo, {myStr}")
print("Un saludo, {0}".format(myStr))





