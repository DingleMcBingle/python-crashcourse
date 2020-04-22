class User():
    """Displays a user's information"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("User info\n" + "First name: " + self.first_name + "\n" + "Last name: " + self.last_name + "\n" + "Age: " + self.age + "\n")

    def greet_user(self):
        print("Hello " + self.first_name + ", How are you today?")