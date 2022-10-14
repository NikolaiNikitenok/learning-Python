# Закрытая зверюшка

# Демонстрирует закрытые переменные и методы


class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, mood):
        print("New Critter!")
        self.name = name  # open
        self.__mood = mood  # close

    def talk(self):
        print("\nМеня зовут", self.name)
        print("Сейчас я чувствую себя", self.__mood, "\n")

    def __private_method(self):
        print("Это закрытый метод.")

    def public_method(self):
        print("Это открытый метод.")
        self.__private_method()


def main():
    crit = Critter("Бобик", "Прекрасно")
    crit.talk()
    crit.public_method()
    input("\n\nPress Enter, pls...")


if __name__ == '__main__':
    main()
