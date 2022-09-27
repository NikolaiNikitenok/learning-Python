# Консервация

# Демонстрирует консервацию данных и доступ к ним через интерфейс полки

import pickle, shelve


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


def main():
    conserve()
    reading()


if __name__ == '__main__':
    main()
