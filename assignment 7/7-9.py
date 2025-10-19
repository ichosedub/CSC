sandwich_orders = ['grilled cheese', 'pastrami', 'chicken salad', 'blt', 'pastrami', 'tuna', 'pb&j', 'pastrami']
print("Unfortunately we have run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

    finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Your {sandwich} sandwich has been prepared.")
    finished_sandwiches.append(sandwich)

print("\nCurrent sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"-{sandwich}")