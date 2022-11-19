from for_users import User
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