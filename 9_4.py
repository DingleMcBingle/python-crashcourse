class Restaurant():
    """Describes a restaurant and tells if it is open."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " serves " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

    def customers_served(self):
        """prints how many customers are served"""
        print("This restaurant has served " + str(self.number_served) + " people.")

    def set_number_served(self,number):
        """sets the number served to whatever is called"""
        self.number_served = number

    def increment_number_served(self, customers):
        self.number_served += customers

restaurant_0 = Restaurant('Al\'s Tavern','Wings')


restaurant_0.set_number_served(150)
restaurant_0.customers_served()
restaurant_0.increment_number_served(100)
restaurant_0.customers_served()