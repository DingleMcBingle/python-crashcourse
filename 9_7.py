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

class Admin(User):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name,last_name,age)
        self.privileges = ['Can ban user', 'can add post', 'can delete post',]

    def show_admin_privileges(self):
        print("Admin privileges:")
        for self.privilege in self.privileges:
            print(self.privilege)



admin_0 = Admin('Adam', 'Mason', '17')
user_1 = User('Ryan', 'Mason', '28')

admin_0.show_admin_privileges()