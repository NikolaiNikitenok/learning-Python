# Переводчик с гикского на русский

# Демонстрирует использование словарей

geek = {"404": "clueless.  From the web error message 404, meaning page not found.",
        "Googling": "searching the Internet for background information on a person.",
        "Keyboard Plaque": "the collection of debris found in computer keyboards.",
        "Link Rot": "the process by which web page links become obsolete.",
        "Percussive Maintenance": "the act of striking an electronic device to make it work.",
        "Uninstalled": "being fired.  Especially popular during the dot-bomb era."}

choice = None

while choice != "0":
    print(
        """
        0 - Выйти
        1 - Найти толкование термина
        2 - Добавить термин
        3 - Изменить толкование
        4 - Удалить термин
        """
    )
    choice = input("Ваш выбор: ")
    print()

    # Выход

    if choice == "0":
        print("До свидания!")

    # Поиск толкования

    elif choice == "1":
        term = input("Какой термин вы хотите перевести с гикского на русский?")
        if term in geek:
            definition = geek[term]
            print("\n", term, "означает", definition)
        else:
            print("\nУвы, этот термин мне незнаком:", term)

    # Добавление термина с толкованием

    elif choice == "2":
        term = input("Какой термин гикского языка вы хотите добавить? ")
        if term not in geek:
            definition = input("\nВпишите ваше толкование: ")
            geek[term] = definition
            print("\nТермин", term, "добавлен в словарь!")
        else:
            print("\nТакой термин уже есть! Попробуйте изменить его толкование.")

