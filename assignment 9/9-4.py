class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} makes {self.cuisine_type}.")

    def amount_served(self, number):
        self.number_served = number

    def served_customers(self, customers):
        self.number_served += customers

restaurant = Restaurant("Cheesecake Factory", "Cheescakes")
restaurant.amount_served(100)
restaurant.served_customers(10)
print(f"Customers served: {restaurant.number_served}")