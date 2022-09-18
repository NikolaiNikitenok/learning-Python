# Арсенал героя 2.0

# Демонстрирует работу с кортежами

# Создадим кортеж с несколькими элементами и выведем его с помощью цикла for

inventory = ("меч",
             "кольчуга",
             "щит",
             "целебное снадобье")
print("\nИтак, в вашем арсенале:")
for item in inventory:
    print(item)
input("\nНажмите Enter, чтобы продолжить.")

# Найдем длину кортежа

print("Сейчас в вашем распоряжении", len(inventory), "предмета/-ов.")
input("\nНажмите Enter, чтобы продолжить.")

# Проверка на принадлежность кортежу с помощью in

if "целебное снадобье" in inventory:
    print("Вы еще поживете и повоюете!")

# Вывод одного предмета с определенным индексом

index = int(input("\nВведите индекс одного из предметов арсенала: "))
print("Под индексом", index, "в арсенале находится", inventory[index])

# Отобразим срез

start = int(input("\nВведите начальный индекс среза: "))
finish = int(input("\nВведите конечный индекс среза: "))
print("Срез inventory[", start, ":", finish, "] - это", end=" ")
print(inventory[start:finish])
input("\nНажмите Enter, чтобы продолжить.")

# Соединим два кортежа

chest = ("золото", "драгоценные камни")
print("Вы нашли ларец. Вот что в нем есть:")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении:")
print(inventory)
input("\nНажмите Enter, чтобы продолжить.")