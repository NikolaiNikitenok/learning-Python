# Телевизор

class Control(object):
    """Пульт управления"""
    def __init__(self, volume=50, chanel=1):
        self.volume = volume
        self.chanel = chanel

    def add_volume(self):
        """Увеличение громкости на 1 пункт"""
        self.volume += 1
        if self.volume > 100:
            self.volume = 100
        print("Громкость:", self.volume)

    def remove_volume(self):
        """Уменьшение громкости на 1 пункт"""
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0
        print("Громкость:", self.volume)

    def add_chanel(self):
        """Увеличение канала на 1 пункт"""
        self.chanel += 1
        if self.chanel > 300:
            self.chanel = 1
        print("Канал:", self.chanel)

    def remove_chanel(self):
        """Уменьшение канала на 1 пункт"""
        self.chanel -= 1
        if self.chanel < 0:
            self.chanel = 300
        print("Канал:", self.chanel)

    def volume1(self, sound):
        """Установка определенной громкости"""
        self.volume = sound

    def volume_plus(self, sound):
        """Добавления определенного кол-ва пунктов громкости"""
        self.volume += sound
        if self.volume >= 100:
            self.volume = 100
        print("Вы добавили звук на", sound, "пунктов!")
        print("Звук сейчас равен:", self.volume)

    def volume_minus(self, sound):
        """Уменьшение определенного кол-ва пунктов громкости"""
        self.volume -= sound
        if self.volume <= 0:
            self.volume = 0
        print("Вы убавили звук на", sound, "пунктов!")
        print("Звук сейчас равен:", self.volume)

    def chanel1(self, punkt):
        """Установка определенного канала"""
        self.chanel = punkt


def main():
    con = Control()

    choice = None
    while choice != "0":
        print(
            """
            Выберете кнопку на пульте, чтобы начать управление телеаизором:
            
            0 - Выход
            1 - Изменить громкость
            2 - Изменить канал
            """
        )
        choice = input("Ваш выбор: ")

        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            choice_volume = None
            while choice_volume != "0":
                print(
                    """
                    Выберете, как вы хотите изменить громкость:
                    
                    0 - Назад
                    1 - "+1" пункт
                    2 - "-1" пункт
                    3 - Установить определенную громкость
                    4 - Добавить определенное кол-во пунктов громкости
                    5 - Убрать определенное кол-во пунктов громкости
                    """
                )

                choice_volume = input("Ваш выбор: ")
                if choice_volume == "0":
                    print("Вы вышли в главное меню!")
                elif choice_volume == "1":
                    con.add_volume()
                elif choice_volume == "2":
                    con.remove_volume()
                elif choice_volume == "3":
                    con.volume1(input("Введите нужное значение громкости: "))
                elif choice_volume == "4":
                    con.volume_plus(int(input("Введите кол-во пунктов, на которое хотите увеличить громкость: ")))
                elif choice_volume == "5":
                    con.volume_minus(int(input("Введите кол-во пунктов, на которое хотите уменьшить громкость: ")))
                else:
                    print("Вы ввели неверную операцию!")
        elif choice == "2":
            choice_chanel = None
            while choice_chanel != "0":
                print(
                    """
                    Выберете, как вы хотите изменить канал:

                    0 - Назад
                    1 - "+1" пункт
                    2 - "-1" пункт
                    3 - Установить определенный канал
                    """
                )
                choice_chanel = input("Ваш выбор: ")
                if choice_chanel == "0":
                    print("Вы вышли в главное меню!")
                elif choice_chanel == "1":
                    con.add_chanel()
                elif choice_chanel == "2":
                    con.remove_chanel()
                elif choice_chanel == "3":
                    con.chanel1(input("Введите нужный канал: "))
                else:
                    print("Вы ввели неверную операцию!")


if __name__ == '__main__':
    main()
