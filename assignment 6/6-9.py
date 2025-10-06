places = {
    'mary': ['greace', 'egypt', 'india'],
    'john': ['jamaica', 'ghana'],
    'timmy': ['italy']
}

for name, places in places.items():
    print(F"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"{places}")