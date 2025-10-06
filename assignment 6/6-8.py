pet0 = {'animal_type': 'snake', 'owner': "Luke"}
pet1 = {'animal_type': 'turtle', 'owner': "Jerry"}
pet2 = {'animal_type': 'ferret', 'owner': "Tom"}

pets = [pet0, pet1, pet2]

for pet in pets:
    print(f"\n{pet['owner']} has a pet {pet['animal_type']}.")