class FFRestaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} makes {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is currently open and serving!")

    def sale_restaurant(self):
        print(f"{self.restaurant_name} has a two for one discount on {self.cuisine_type}!")


fastfoodrestaurant1 = FFRestaurant("Mcdonalds", "Burgers")
fastfoodrestaurant2 = FFRestaurant("Chipotle", "Burritos")
fastfoodrestaurant3 = FFRestaurant("Taco Bell", "Tacos")

fastfoodrestaurant1.describe_restaurant()
fastfoodrestaurant2.open_restaurant()
fastfoodrestaurant3.sale_restaurant()

