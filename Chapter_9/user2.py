# Users 2.0

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


class Privileges():
    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]
    def show_privileges(self):
        print(f"You are Admin! \n You can: ")
        for priv in self.privileges:
            print(priv.title())

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
        self.privileges.show_privileges()
        
    
        

def main():
    # user1 = User(input("Your name: "), input("Your Last name: "))
    # user1.describe_user()
    # user1.greet_user()
    # user1.increment_login_attempts()
    # user1.increment_login_attempts()
    # user1.increment_login_attempts()
    # user1.increment_login_attempts()
    # user1.reset_login_attempts()
    admin1 = Admin("Nikolai", "Nikitenok")
    admin1.describe_user()
    
    

if __name__ == "__main__":
    main()