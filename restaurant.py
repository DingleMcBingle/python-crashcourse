class Restaurant():
    """Describes a restaurant and tells if it is open."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " serves " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")