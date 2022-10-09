# Просто зверюшка
# Демонстрирует простейшие класс и объект


def main():
    class Critter(object):
        """Виртуальный питомец"""
        def talk(self):
            print("Привет. Я зверюшка - экземпляр класса Critter.")
    
    
    # Основная часть

    crit = Critter()
    crit.talk()
    input("\n\nPress Enter, please...")


if __name__ == "__main__":
    main()
