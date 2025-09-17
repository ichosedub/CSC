my_pizzas = ['pepperoni', 'cheese', 'NY style', 'shrimp']
friends_pizzas = my_pizzas[:]

my_pizzas.append('meatlovers')
friends_pizzas.append('veggie')

print("My favorite pizzas are:")
for pizzas in my_pizzas:
        print(pizzas.title())

print("\nMy friend's favorite pizzas are:")
for pizzas in friends_pizzas:
        print(pizzas.title())