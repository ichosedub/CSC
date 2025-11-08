class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} makes {self.cuisine_type}.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "cookies&cream", "coffee", "mint"]

    def menu_flavors(self):
        print(f"{self.restaurant_name} serves these flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
stand = IceCreamStand("FrozenPeaks")
stand.describe_restaurant()
stand.menu_flavors()