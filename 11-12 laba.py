def z111():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Restaurant Name: {self.restaurant_name}")
            print(f"Cuisine Type: {self.cuisine_type}")

        def open_restaurant(self):
            print("Restaurant is open!")

    newRestaurant = Restaurant("BestBites", "Italian")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
z111()
def z112():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Restaurant Name: {self.restaurant_name}")
            print(f"Cuisine Type: {self.cuisine_type}")

    a = Restaurant("TastePalace", "Rassia")
    b = Restaurant("FainaUkraina", "Ukraine")
    c = Restaurant("HappyPlace", "London")
    print(a.describe_restaurant())
    print(b.describe_restaurant())
    print(c.describe_restaurant())

def z113():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating = 0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            salf.rating = rating

        def describe_restaurant(self):
            description = f"ресторан '{self. restaurant_name}' кухня '{self.cuisine_type}' рейтинг '{self.rating}"
            return description
        def update_rating(self, new_rating):
            self.rating = new_rating
            return {"Рейтинг ресторана '{self.restaurant_name}' рейтинг обновлен: {self.rating}"
a = Restaurant ("aliot", "London" , 3,5)
            print (a.describe_restauranta())
            new_rating = 4.5
            update_message = a.update_rating (new_rating)
            print(update_message)

def z121():
    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors=[]):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def display_flavors(self):
            print("Available Flavors:")
            for flavor in self.flavors:
                print(flavor)

    iceCreamStand = IceCreamStand("IceDreams", "Ice Cream", ["Chocolate", "Vanilla", "Strawberry"])
    iceCreamStand.describe_restaurant()
    iceCreamStand.display_flavors()

    def z122():
        class IceCreamStand(Restaurant):
            def __init__(self, restaurant_name, cuisine_type, flavors=[], location="", working_hours=""):
                super().__init__(restaurant_name, cuisine_type)
                self.flavors = flavors
                self.location = location
                self.working_hours = working_hours

            def display_info(self):
                print(f"Restaurant Name: {self.restaurant_name}")
                print(f"Cuisine Type: {self.cuisine_type}")
                print("Available Flavors:")
                for flavor in self.flavors:
                    print(flavor)
                print(f"Location: {self.location}")
                print(f"Working Hours: {self.working_hours}")

        iceCreamStand = IceCreamStand("IceDreams", "Ice Cream", ["Chocolate", "Vanilla", "Strawberry"], "123 Main St",
                                      "10:00AM -9:00PM")
        iceCreamStand.display_info()
