# Арсенал героя

# Демонстрирует создание кортежа

# Создадим пустой кортеж

inventory = ()

# Теперь создадим кортеж с несколькими элементами

if not inventory:
    print("Вы безоружны!")
input("\nНажмите Enter, чтобы продолжить.")

# Теперь создадим кортеж с несколькими элементами

inventory = ("меч",
             "кольчуга",
             "щит",
             "целебное снадобье")

# Выведем этот кортеж на экран

print("\nСодержимое кортежа:")
print(inventory)

# Выведем все элементы последовательно

print("\nИтак, в вашем арсенале:")
for item in inventory:
    print(item)

