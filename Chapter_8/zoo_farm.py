# Зооферма

# Создается несколько зверюшек, управление через список, случайные показатели голода и настроения при создании, \
# выполнения действий со всеми зверюшками сразу

import random


class Critter(object):

    total = 0

    critter_list = []

    def __init__(self, name, breed, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.breed = breed
        Critter.total += 1
        Critter.critter_list.append(self.name)

    def delik(self):
        """Удаление зверюшки"""


    def __str__(self):
        stat = f"\nName: {self.name}, \nHunger: {self.hunger}, \nBoredom: {self.boredom}, \nПорода: {self.breed}"
        return stat

    @staticmethod
    def status():
        print(f"\nВсего зверюшек в вашем зоопарке: {Critter.total}")
        print(f"\nВот список зверюшек: {Critter.critter_list}")


def main():
    choice = None

    print(
        """
        Добро пожаловать в зоопарк!
        """
    )

    while choice != "0":
        Critter.status()
        print(
            """
            Вы можете выбрать действие:
            
            0 - Выход
            1 - Добавить/Удалить зверюшку
            2 - Узнать состояние зверюшки
            3 - Покормить зверюшку
            4 - Поиграть со зверюшкой
            """
        )
        choice = input("Введите ваш выбор: ")

        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            choice_edit = None
            Critter.status()
            print(
                """
                Можете выбрать:
                0 - Назад
                1 - Добавить зверюшку
                2 - Удалить зверюшку
                """
            )

            while choice_edit != "0":
                choice_edit = input("Ваш выбор: ")

                if choice_edit == "0":
                    "Вы вернулись в главное меню!"

                elif choice_edit == "1":
                    print("Вы выбрали добавить зверюшку!")

                    crit = Critter(input("Введите имя зверюшки: "), input("Введите породу зверюшки: "))
                    print(crit)

                    Critter.status()


if __name__ == '__main__':
    main()
