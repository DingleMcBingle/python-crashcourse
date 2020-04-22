class Restaurant():
    """Describes a restaurant and tells if it is open."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " serves " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

restaurant_0 = Restaurant('Al\'s Tavern','Wings')
restaurant_1 = Restaurant('Red Lobster', 'Seafood')
restaurant_2 = Restaurant('Jack & Georges', 'Pizza')

restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()