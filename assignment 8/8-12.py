def sandwiches(*ingredients):
    print("\nI want to make a sandwich with:")
    for ingredient in ingredients:
        print(f".{ingredient}.")

sandwiches("chicken", "cheese", "fruits")
sandwiches("pork", "vegitables")
sandwiches("crab", "nutella")