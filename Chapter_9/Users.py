# Users

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"Это {self.first_name} {self.last_name}")
        
    def greet_user(self):
        print(f"Привет, дорогой {self.first_name} {self.last_name}!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Кол-во попыток: {self.login_attempts}!")
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Кол-во попыток: {self.login_attempts}!")


def main():
    user1 = User(input("Your name: "), input("Your Last name: "))
    user1.describe_user()
    user1.greet_user()
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.reset_login_attempts()
    

if __name__ == "__main__":
    main()
