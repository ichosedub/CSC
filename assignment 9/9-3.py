class User:
    def __init__(self, first_name, last_name, phone_number, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, {self.phone_number}, lives at {self.address}")

    def greet_user(self):
        print(f"Welcome Mr.{self.last_name}!")


user1 = User("Kylie", "Townlie", 2155673498, "1801 N 13th St, Reading, PA 19604, United States")
user2 = User("Angel", "Wawkins", 6784231099, "1801 N 13th St, Reading, PA 19604, United States")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()