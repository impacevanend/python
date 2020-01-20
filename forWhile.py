foods = ["apples", "bread", "cheese", "milk","banana","grapes"]

print(foods[3])

#Bucles para consultar lista de datos

for food in foods:

    if food == "cheese":

        print(f"\nYou have to buy this, {food}!")

        #break(termina la ejecución.)
        #continue(salta y registra los de mas.)

    print(f"\nEste elemento, {food}")

