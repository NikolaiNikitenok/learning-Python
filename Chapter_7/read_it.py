# Прочитаем файл

# Демонстрирует чтение из текстового файла


def open_close():
    print("Открываю и закрываю файл.")
    text_file = open("read_it.txt", "r", encoding='utf-8')
    text_file.close()


def file_symbol():
    print("\nЧитаю файл посимвольно.")
    text_file = open("read_it.txt", "r")
    print(text_file.read(1))
    print(text_file.read(5))
    text_file.close()


def file_full():
    print("\nЧитаю файл целиком.")
    text_file = open("read_it.txt", "r", encoding="utf-8")
    whole_thing = text_file.read()
    print(whole_thing)
    text_file.close()


def line_symbol():
    print("\nЧитаю одну строку посимвольно.")
    text_file = open("read_it.txt", "r", encoding="utf-8")
    print(text_file.readline(1))
    print(text_file.readline(5))
    text_file.close()


def line_full():
    print("\nЧитаю одну строку целиком.")
    text_file = open("read_it.txt", "r", encoding="utf-8")
    print(text_file.readline())
    print(text_file.readline())
    print(text_file.readline())
    text_file.close()


def file_in_list():
    print("\nЧитаю весь файл в список.")
    text_file = open("read_it.txt", "r", encoding="utf-8")
    lines = text_file.readlines()
    print(lines)
    print(len(lines))
    for line in lines:
        print(line)
    text_file.close()


def file_in_lines():
    print("\nПеребираю файл построчно.")
    text_file = open("read_it.txt", "r", encoding="utf-8")
    for line in text_file:
        print(line)
    text_file.close()
    input("\n\nPlease Enter...")


def main():
    open_close()
    file_symbol()
    file_full()
    line_symbol()
    line_full()
    file_in_list()
    file_in_lines()


if __name__ == '__main__':
    main()
