# Ресторан
from for_restaurant import Restaurant as r
from for_restaurant import IceCreamStand as ICS


# class IceCreamStand(r):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ["Сливочное", "Фисташковое", "Шоколадное"]

#     def describe_stand(self):
#         print("У нас в ассортименте есть: ")
#         for flavor in self.flavors:
#             print(flavor)


def main():
    rest1 = r("Biba", "German")
    rest2 = r("Boba", "Korean")
    rest1.describe_restaurant()
    rest2.describe_restaurant()
    rest1.open_restaurant()
    rest2.open_restaurant()
    print(rest1.number_served)
    rest1.number_served = 300
    print(rest1.number_served)
    rest1.set_number_served(500)
    stand1 = ICS("Bongo", "Ice")
    stand1.describe_restaurant()
    stand1.describe_stand()
    print(rest1.number_served)
    rest1.increment_number_served()
    print(rest1.number_served)

    
if __name__ == "__main__":
    main()
        