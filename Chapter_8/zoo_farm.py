# Зооферма

# Создается несколько зверюшек, управление через список, случайные показатели голода и настроения при создании, \
# выполнения действий со всеми зверюшками сразу

import random


class Critter(object):

    total = 0

    critter_list = []

    def __init__(self, name, breed, hunger, boredom):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.breed = breed
        Critter.total += 1
        # Critter.critter_list.append(self.name)

    def talk(self):
        print(f"Меня зовут {self.name}. Я чувствую себя: {self.mood}")

    def __str__(self):
        stat = f"\nName: {self.name}, \nHunger: {self.hunger}, \nBoredom: {self.boredom}, \nПорода: {self.breed}"
        return stat

    @staticmethod
    def status():
        print(f"\nВсего зверюшек в вашем зоопарке было: {Critter.total}")
        # print(f"\nВот список зверюшек: {Critter.critter_list}")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "Прекрасно"
        elif 6 <= unhappiness <= 10:
            m = "Неплохо"
        elif 11 <= unhappiness <= 15:
            m = "Не сказать, что хорошо"
        elif unhappiness >= 16:
            m = "Ужасно!"
        return m

    def eat(self, food):
        print("Ммм... Вкусно!")
        self.hunger -= food
        if self.hunger <= 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, time):
        print("Ммм... Вкусно!")
        self.boredom -= time
        if self.boredom <= 0:
            self.boredom = 0
        self.__pass_time()

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

def main():
    choice = None
    zoo = []
    zoo_mood = []

    print(
        """
        Добро пожаловать в зоопарк!
        """
    )

    while choice != "0":
        Critter.status()

        # Список с именами зверюшек
        print("Список зверей, находящихся в зоопарке: ")
        for n in zoo:
            print(n)


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
                    print("Вы вернулись в главное меню!")

                elif choice_edit == "1":
                    print("Вы выбрали добавить зверюшку!")

                    crit = Critter(input("Введите имя зверюшки: "), input("Введите породу зверюшки: "),\
                                   random.randint(0, 5), random.randint(0, 5))
                    zoo.append(crit.name)
                    zoo_mood.append(crit)

                    print("Вывод 1 элемента: ", zoo[0])

                    Critter.status()

                elif choice_edit == "2":
                    zver = input("Выберете зверюшку из списка, которую хотите удалить! Просто введите её имя: ")

                    if zver in zoo:
                        zoo.remove(zver)
                        print("Вы удалили зверюшку с именем: ", zver, "!\n")
                    else:
                        print("Нет такого имени!")

        elif choice == "2":
            for i in zoo_mood:
                Critter.talk(i)

        elif choice == "3":
            print(
                """
                Вы хотите накормить всех своих зверюшек в зоопарке! \n
                """
            )
            food = input("Выберете кол-во еды, которое вы хотите скормить: ")
            Critter.eat(food)


if __name__ == '__main__':
    main()
