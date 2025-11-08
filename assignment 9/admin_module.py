class Admin:
    def __init__(self, first_name, last_name, status):
        self.first_name = first_name
        self.last_name = last_name
        self.status = status

    def greet_user(self):
        print(f"Welcome Mr.{self.last_name}!")

class User_Privileges:
    def __init__(self):
        self.privileges = ["can: delete", "ban", "timeout"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class SuperAdmin(Admin):
    def __init__(self, first_name, last_name, status):
        super().__init__(first_name, last_name, status)
        self.privileges = User_Privileges()