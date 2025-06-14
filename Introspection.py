##introspection ability to introspect the code and get information about the classes, methods, and attributes

## dir - shows all methods and attributes of an object
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power {self.power}")


wizard1 = Wizard("Merlin", 50, "merling@hot.com")

print(dir(wizard1.email))