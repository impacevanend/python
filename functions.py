#Definición de una función
name = "George" 

def hello(nam = "Person"):

    print(f"HELLO WORLD:{name}")

hello(name)

def add(num1,num2):

    sum = num1 + num2

    return print(sum)


add(2,3)

mul = lambda num1, num2: num1 * num2

print(mul(100, 2))
