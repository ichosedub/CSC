from user_module import User

class Privileges:
    def __init__(self):
        self.privileges = ["can delete posts", "can ban users", "can moderate chat"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

