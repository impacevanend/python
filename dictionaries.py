#* Nos permite definir un elemento a través de claves y valores.

product = {
    "name":"book",
    "quantity":3,
    "price":4.99
}

person = {
    "firstName":"Jose",
    "LastName":"Tang"
}

#*Tipo de dato
print(type(product))

#*Tipos de propiedades y métodos
print(dir(product))

#*Conocer las llaves del diccionario.

print(person.keys()) 

#*Conocer los items

print(person.items()) 

#*Eliminar diccionario

# del person

# print(person)

#*Eliminar elementos internos del diccionario.

print(f"Los elementos internos de {person}")
person.clear()
print(f"Lo elementos des pues de utilizar el método {person}")

items = [
    {"name":"book", "price":12.54},
    {"name": "laptop", "price":120.54}
]
    


print(items)
 