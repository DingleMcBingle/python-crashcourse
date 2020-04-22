class User():
    """Displays a user's information"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("User info\n" + "First name: " + self.first_name + "\n" + "Last name: " + self.last_name + "\n" + "Age: " + self.age + "\n")

    def greet_user(self):
        print("Hello " + self.first_name + ", How are you today?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def print_login_attempts(self):
        print("This user had " + str(self.login_attempts) + " login attempts.")

user_0 = User('Adam', 'Mason', '17')
user_1 = User('Ryan', 'Mason', '28')

user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.print_login_attempts()
user_0.reset_login_attempts()
user_0.print_login_attempts()