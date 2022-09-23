# День рождения

# Демонстрирует именованные аргументы и значения параметров по умолчанию

# позиционные параметры
def birthday1(name, age):
    print(
        "С днем рождения,", name, "!", " Вам сегодня исполняется", age, ", не так ли?\n"
    )


# end def

# Параметры со значением по умолчанию
def birthday2(name="товарищ Иванов", age=1):
    print(
        "С днем рождения,", name, "!", " Вам сегодня исполняется", age, ", не так ли?\n"
    )


# end def

birthday1("товарищ Иванов", 1)
birthday1(1, "товарищ Иванов")
birthday1(name="товарищ Иванов", age=1)
birthday1(age=1, name="товарищ Иванов")
birthday2()
birthday2(name="Катя")
birthday2(age=12)
birthday2(name="Катя", age=12)
birthday2("Катя", 12)
input("\n\nPress Enter!")
