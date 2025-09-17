my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for foods in my_foods:
        print(foods.title())

print("My friend loves:")
for food in friend_foods:
        print(f"I love to eat {food}!")