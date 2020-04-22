class Privileges():

    def __init__(self, privileges = ['Can ban user', 'can add post', 'can delete post']):
        self.privileges = privileges

    def show_admin_privileges(self):
        print("Admin privileges:")
        for self.privilege in self.privileges:
            print(self.privilege)

class Admin(User):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name,last_name,age)
        self.show_priviliges = Privileges()
        