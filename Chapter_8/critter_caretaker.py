# Моя зверюшка

# Виртуальный питомец, о котором пользователь может заботиться

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        stat = f"Голод: {self.hunger} \n"
        stat += f"Настроение: {self.boredom} \n"
        return stat

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "Прекрасно"
        elif 6 <= unhappiness <= 10:
            m = "Неплохо"
        elif 11 <= unhappiness <= 15:
            m = "Не сказать, чтобы хорошо"
        else:
            m = "Ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood, ".\n")
        self.__pass_time()

    def eat(self, food):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Как вы назовете свою зверюшку? ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print(
                """
                Моя зверюшка
                0 - Выйти
                1 - Узнать о самочувствии зверюшки
                2 - Покормить зверюшку
                3 - Поиграть со зверюшкой
                """
            )
        choice = input("Ваш выбор: ")
        print()
        # Выход
        if choice == "0":
            print("До свидания!")

        # Беседа со зверюшкой
        elif choice == "1":
            crit.talk()

        # Кормление зверюшки
        elif choice == "2":
            print("Введите кол-во еды, которое хотите дать зверюшке:", end=" ")
            food = int(input())
            crit.eat(food)

        # Игра со зверюшкой
        elif choice == "3":
            fun = int(input("Введите кол-во времени, которое поиграете со зверюшкой (от 1 до 4 минут): "))
            crit.play(fun)

        # Черных ход - проверка хар-ик
        elif choice == "admin":
            print(crit)

        # Непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)


if __name__ == '__main__':
    main()
