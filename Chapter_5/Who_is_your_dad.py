# Кто твой папа?

# Программа пишет отца, при написании сына
# есть возможность добавления, изменения и удаления пар

dictionary = {"Сын": "Отец",
              "Отец": "Дед",1

              "Никитенок Николай Александрович": {"Никитенок Александр Сергеевич": "Никитенок Сергей Владимирович"},
              "Петров Петр Олегович": "Петров Олег Геннадиевич"}
choice = None
while choice != "0":
    choice = input("Выберете: 1 - Найти, 2 - Добавить, 3 - Изменить, 4 - Удалить: ")
    if choice == "0":
        print("До свидания!")
    elif choice == "1":
        sin = input("Введите ФИО сына: ")
        if sin in dictionary:
            print(dictionary[sin])
    elif choice == "2":
        sin = input("name sin: ")
        dad = input("name dad: ")
        dictionary[sin] = dad
    elif choice == "3":
        sin = input("choose sin for edit: ")
        dad = input("name dad: ")
        dictionary[sin] = dad
    elif choice == "4":
        sin = input("choose sin for delete: ")
        del dictionary[sin]

