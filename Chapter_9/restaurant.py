# Ресторан

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}; \nТип ресторана: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name}, открыт!")
        
        
def main():
    rest1 = Restaurant("Biba", "German")
    rest2 = Restaurant("Boba", "Korean")
    rest1.describe_restaurant()
    rest2.describe_restaurant()
    rest1.open_restaurant()
    rest2.open_restaurant()
    
if __name__ == "__main__":
    main()
        