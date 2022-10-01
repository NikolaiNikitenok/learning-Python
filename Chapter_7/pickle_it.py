# Консервация

# Демонстрирует консервацию данных и доступ к ним через интерфейс полки

import pickle
import shelve


def conserve():
    print("Консервация списков.")
    variety = ["Огурцы", "Помидоры", "Капуста"]
    shape = ["Целые", "Кубиками", "Соломкой"]
    brand = ["Главпродукт", "Чумак", "Бондюэль"]
    f = open("pickles1.dat", "wb")
    pickle.dump(variety, f)
    pickle.dump(shape, f)
    pickle.dump(brand, f)


def reading():
    print("\nРасконсервация списков.")
    f = open("pickles1.dat", "rb")
    variety = pickle.load(f)
    shape = pickle.load(f)
    brand = pickle.load(f)
    print(variety)
    print(shape)
    print(brand)
    f.close()


def shelving():
    print("\nПомещение списков на полку.")
    s = shelve.open("pickles2.dat")
    s["variety"] = ["Огурцы", "Помидоры", "Капуста"]
    s["shape"] = ["Целые", "Кубиками", "Соломкой"]
    s["brand"] = ["Главпродукт", "Чумак", "Бондюэль"]
    s.sync()  # Убедимся, что данные записаны

    # Извлечение
    print("\nИзвлечение списков из файлов полки.")
    print("Торговые марки -", s["brand"])
    print("Формы -", s["shape"])
    print("Виды овощей -", s["variety"])
    s.close()
    input("Please Enter.")


def main():
    conserve()
    reading()
    shelving()


if __name__ == '__main__':
    main()
