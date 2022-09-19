# Рекорды 2.0

# Демонстрирует вложенные последовательности

scores = []
choice = None

while choice != "0":
    print(
        """
        0 - Выйти
        1 - Показать рекорды
        2 - Добавить рекорд
        """
    )
    choice = input("Ваш выбор: ")
    print()

    # Выход

    if choice == "0":
        print("До свидания!")

    # Вывод таблицы рекордов

    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # Добавление рекорда

    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Введите его результат: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]  # В списке остается только 5 рекордов

    # непонятный пользовательский ввод

    else:
        print("Извините, в меню нет пункта", choice)

input("\n\nНажмите Enter, чтобы выйти.")
