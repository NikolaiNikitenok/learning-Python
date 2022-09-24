# Отгадай число (С использованием функций)

import random


def welcome():
    print("\tДобро пожаловать в игру 'Отгадай число'!")
    print("\nПравила игры:")
    print("\nЯ загадал натурально число из диапазона от 1 до 100.")
    print("\nПостарайтесь отгадать его за минимальное кол-во попыток.\n")


def create_number(low, high):
    number = random.randint(low, high)
    return number, low, high


def ask_number(question, low, high):
    """Просит ввести число из диапазона угадывания."""
    guess = None
    while guess not in range(low, high):
        guess = int(input(question))
        return guess


def check_number(number, guess, low, high):

    tries = 0
    while guess != number:
        tries += 1
        if guess < number:
            print("Ваше предположение меньше загаданного числа!")
            print("Вы уже потратили:", tries, "попыток.")
        elif guess > number:
            print("Ваше предположение больше загаданного числа!")
            print("Вы уже потратили:", tries, "попыток.")
        guess = ask_number(f"Введите число от {low} до {high}: ", low, high)
    print("Урааа! Вы угадали!")


def main():
    welcome()
    number, low, high = create_number(0, 100)
    guess = ask_number(f"Введите число от {low} до {high}: ", low, high)
    check_number(number, guess, low, high)


if __name__ == "__main__":
    main()
