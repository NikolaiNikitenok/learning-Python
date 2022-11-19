class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}; \nТип ресторана: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name}, открыт!")
        
    def set_number_served(self, number):
        self.number_served = number
        
    def increment_number_served(self):
        self.number_served += 1
        
        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Сливочное", "Фисташковое", "Шоколадное"]

    def describe_stand(self):
        print("У нас в ассортименте есть: ")
        for flavor in self.flavors:
            print(flavor)
