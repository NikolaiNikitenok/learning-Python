# Запишем

# Демонстрирует запись в текстовый файл


def create():
    print("Создаю текстовый файл методом write().")
    text_file = open("write_it.txt", "w", encoding="utf-8")
    text_file.write("Строка 1\n")
    text_file.write("Это строка 2\n")
    text_file.write("Этой строке достался номер 3\n")
    text_file.close()


def reading():
    print("\nЧитаю вновь созданный файл.")
    text_file = open("write_it.txt", "r", encoding="utf-8")
    print(text_file.read())
    text_file.close()


def create_list_with_lines():
    text_file = open("write_it.txt", "w", encoding="utf-8")
    lines = [
        "Строка 1\n",
        "Это строка 2\n",
        "Этой строке достался номер 3\n"
    ]
    text_file.writelines(lines)
    text_file.close()


def main():
    create()
    reading()
    create_list_with_lines()
    reading()


if __name__ == '__main__':
    main()
