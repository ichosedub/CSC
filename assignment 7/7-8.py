sandwich_orders = ['grilled cheese', 'chicken salad', 'blt', 'tuna', 'pb&j']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Your {sandwich} sandwich has been prepared.")
    finished_sandwiches.append(sandwich)

print("\nCurrent sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"-{sandwich}")