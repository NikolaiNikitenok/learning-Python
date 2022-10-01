# Викторина
# Игра на выбор правильного варианта ответа.
# Вопросы которой читаются из текстового файла

import sys
import pickle


def open_file(file_name, mode):
    """Открывает файл"""
    try:
        the_file = open(file_name, mode, encoding="utf-8")
    except IOError as e:
        print("Невозможно открыть файл", file_name, ", работа программы будет завершена.\n", e)
        input("\n\nPlease Enter...")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла."""
    category = next_line(the_file)
    question = next_line(the_file)
    answer = []
    for i in range(4):
        answer.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    # nominal question's
    nominal = next_line(the_file)

    explanation = next_line(the_file)
    return category, question, answer, correct, nominal, explanation


def welcome(title):
    """Приветствует игрока и сообщает тему игры."""
    print("\t\tДобро пожаловать в игру 'Викторина'!\n")
    print("\t\t", title, "\n")


def ur_name():
    name = input("Введите ваше имя: ")
    return name


def save_progress(name, score):

    # Conserve
    new_file = open("results.dat", "ab")
    pickle.dump(name, new_file)
    pickle.dump(score, new_file)

    # Text file
    print("Saving progress... Wait...")
    new_file = open("results.txt", "a", encoding="utf-8")
    new_file.write(name)
    new_file.write("\t")
    new_file.write(score)
    new_file.write("\n")
    print("Saved!")


def main():
    name = ur_name()
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # Извлечение первого блока
    category, question, answers, correct, nominal, explanation = next_block(trivia_file)
    while category:
        # вывод вопроса на экран
        print(category)
        print(question)

        # question's nominal
        print("Стоимость вопроса: ", nominal)

        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # Получение ответа
        answer = input("Ваш ответ: ")

        # Проверка ответа
        if answer == correct:
            print("\nДа!", end=" ")
            score += int(nominal)
        else:
            print("\nНет!", end=" ")
        print(explanation)
        print("Счет:", score, "\n\n")

        # Переход к следующему вопросу
        category, question, answers, correct, nominal, explanation = next_block(trivia_file)
    trivia_file.close()
    print("Это был последний вопрос!")
    print("На вашем счету", score)

    score = str(score)

    # Сохранение прогресса
    save_progress(name, score)


if __name__ == '__main__':
    main()
