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
            self.chanel = 0
        print("Канал:", self.chanel)

    def volume(self, sound):
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

    def chanel(self, punkt):
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
            while



if __name__ == '__main__':
    main()
