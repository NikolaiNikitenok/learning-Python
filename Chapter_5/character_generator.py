# Генератор персонажей
# дается 30 очков, чтобы распределить их на 4 навыка персонажа

# Dict with skills
skills = {
    "Strength": 0,
    "Health": 0,
    "Wisdom": 0,
    "Dexterity": 0
}

for i, j in skills.items():
    print(i, j)

# Добавляем кол-во очков

points = 30

# Start

choice = None


while choice != "0":
    print("Характеристики вашего персонажа: ", skills)
    print("\nВы можете распределить", points, "очков, для прокачивания умений своего персонажа!")

    print(
        """
        Выберете умение, которому хотите изменить значение: 

        1 - Strength
        2 - Health
        3 - Wisdom
        4 - Dexterity

        0 - Выход
        """
    )

    choice = input("Введите ваш выбор: ")

    choice_editor = None
    choice_editor2 = None
    choice_editor3 = None
    choice_editor4 = None

    # Выход

    if choice == "0":
        print("До свидания!")

    elif choice == "1":
        while choice_editor != "0":
            print("Вы выбрали редактирование \"Strength\":")
            print("\nУ вас", points, "очков.")
            if points <= 0:
                print("У вас закончились очки навыков!")
            print(
                """
                1 - Добавить очков к этому умению
                2 - Убавить очки для этого умения
                
                0 - Выйти из настройки этого умения
                """
            )
            choice_editor = input("Что вы хотите сделать? ")

            # Выход из редактирования

            if choice_editor == "0":
                print("Вы вышли из редактора навыка!")

            elif choice_editor == "1":
                quantity = skills["Strength"]
                points_plus = int(input("Введите, сколько вы хотите добавить очков к умению: "))
                quantity += points_plus
                skills["Strength"] = quantity
                points -= points_plus

            elif choice_editor == "2":
                quantity = skills["Strength"]
                points_minus = int(input("Введите, сколько вы хотите удалить очков у умения: "))
                quantity -= points_minus
                skills["Strength"] = quantity
                points += points_minus

    elif choice == "2":
        while choice_editor2 != "0":
            print("Вы выбрали редактирование \"Health\":")
            print("\nУ вас", points, "очков.")
            if points <= 0:
                print("У вас закончились очки навыков!")
            print(
                """
                1 - Добавить очков к этому умению
                2 - Убавить очки для этого умения

                0 - Выйти из настройки этого умения
                """
            )
            choice_editor2 = input("Что вы хотите сделать? ")

            # Выход из редактирования

            if choice_editor2 == "0":
                print("Вы вышли из редактора навыка!")

            elif choice_editor2 == "1":
                quantity = skills["Health"]
                points_plus = int(input("Введите, сколько вы хотите добавить очков к умению: "))
                quantity += points_plus
                skills["Health"] = quantity
                points -= points_plus

            elif choice_editor2 == "2":
                quantity = skills["Health"]
                points_minus = int(input("Введите, сколько вы хотите удалить очков у умения: "))
                quantity -= points_minus
                skills["Health"] = quantity
                points += points_minus

    elif choice == "3":
        while choice_editor3 != "0":
            print("Вы выбрали редактирование \"Wisdom\":")
            print("\nУ вас", points, "очков.")
            if points <= 0:
                print("У вас закончились очки навыков!")
            print(
                """
                1 - Добавить очков к этому умению
                2 - Убавить очки для этого умения

                0 - Выйти из настройки этого умения
                """
            )
            choice_editor3 = input("Что вы хотите сделать? ")

            # Выход из редактирования

            if choice_editor3 == "0":
                print("Вы вышли из редактора навыка!")

            elif choice_editor3 == "1":
                quantity = skills["Wisdom"]
                points_plus = int(input("Введите, сколько вы хотите добавить очков к умению: "))
                quantity += points_plus
                skills["Wisdom"] = quantity
                points -= points_plus

            elif choice_editor3 == "2":
                quantity = skills["Wisdom"]
                points_minus = int(input("Введите, сколько вы хотите удалить очков у умения: "))
                quantity -= points_minus
                skills["Wisdom"] = quantity
                points += points_minus

    elif choice == "4":
        while choice_editor4 != "0":
            print("Вы выбрали редактирование \"Dexterity\":")
            print("\nУ вас", points, "очков.")
            if points <= 0:
                print("У вас закончились очки навыков!")
            print(
                """
                1 - Добавить очков к этому умению
                2 - Убавить очки для этого умения

                0 - Выйти из настройки этого умения
                """
            )
            choice_editor4 = input("Что вы хотите сделать? ")

            # Выход из редактирования

            if choice_editor4 == "0":
                print("Вы вышли из редактора навыка!")

            elif choice_editor4 == "1":
                quantity = skills["Dexterity"]
                points_plus = int(input("Введите, сколько вы хотите добавить очков к умению: "))
                quantity += points_plus
                skills["Wisdom"] = quantity
                points -= points_plus

            elif choice_editor4 == "2":
                quantity = skills["Dexterity"]
                points_minus = int(input("Введите, сколько вы хотите удалить очков у умения: "))
                quantity -= points_minus
                skills["Wisdom"] = quantity
                points += points_minus
