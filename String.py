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

