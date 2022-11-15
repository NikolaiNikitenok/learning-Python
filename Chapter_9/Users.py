# Users

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        print(f"Это {self.first_name} {self.last_name}")
        
    def greet_user(self):
        print(f"Привет, дорогой {self.first_name} {self.last_name}!")
        

def main():
    user1 = User(input("Your name: "), input("Your Last name: "))
    user1.describe_user()
    user1.greet_user()


if __name__ == "__main__":
    main()
