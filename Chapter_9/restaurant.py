# Ресторан

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


def main():
    rest1 = Restaurant("Biba", "German")
    rest2 = Restaurant("Boba", "Korean")
    rest1.describe_restaurant()
    rest2.describe_restaurant()
    rest1.open_restaurant()
    rest2.open_restaurant()
    print(rest1.number_served)
    rest1.number_served = 300
    print(rest1.number_served)
    rest1.set_number_served(500)
    stand1 = IceCreamStand("Bongo", "Ice")
    stand1.describe_restaurant()
    stand1.describe_stand()
    print(rest1.number_served)
    rest1.increment_number_served()
    print(rest1.number_served)

    
if __name__ == "__main__":
    main()
        