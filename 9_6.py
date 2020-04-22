class Restaurant():
    """Describes a restaurant and tells if it is open."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " serves " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla','chocolate','strawberry','peanut butter']

    def list_flavors(self):
        print("Flavors include: ")
        for self.flavor in self.flavors:
            print(self.flavor)


restaurant_0 = Restaurant('Al\'s Tavern','Wings',)

icecream_0 = IceCreamStand('Frosty Cow', 'Ice cream',)
icecream_0.list_flavors()