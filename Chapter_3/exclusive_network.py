# Эксклюзивная сеть

# Демонстрирует составные условия и логические операторы

print("\tЭксклюзивная компьютерная сеть")
print("\tТолько для зарегистрированных пользователей!\n")
security = 0
username = ''
while not username:
    username = input('Логин: ')
password = ''
while not password:
    password = input('Пароль: ')
if username == 'nikitenok' and password == 'admin':
    print('Привет, Николай, мы вас заждались!')
    security = 5
elif username == 'mozhaev' and password == 'nikita228':
    print("Привет, Никита. Как дела?")
    security = 3
elif username == 'guest' or password == 'guest':
    print("Добро пожаловать к нам в гости!")
    security = 1
else:
    print("Войти не удалось! Видимо, вы не очень-то эксклюзивный гражданин.\n")
