# Принимай-возвращай
# Демонстрирует параметры и возвращение значения

def display(message):
    print(message)


def give_me_five():
    five = 5
    return five


def ask_yes_no(question):
    """Задает вопрос ответом \"да\" или \"нет\"."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

# Основная часть

display("Вам сообщение.\n")
number = give_me_five()
print("Вот что возратила функция give_me_five():", number)
answer = ask_yes_no("\nПожалуйста, введите 'y' или 'n': ")
print("Спасибо, что ввели", answer)

input("\n\nНажмите Enter, чтобы выйти.")
