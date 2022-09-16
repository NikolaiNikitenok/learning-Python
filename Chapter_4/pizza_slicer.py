# Резчик пиццы

# Демонстрирует срезы строк

word = "pizza"
print(
    """
    Памятка
    0   1   2   3   4   5 
    +---+---+---+---+---+ 
    | p | i | z | z | a | 
    +---+---+---+---+---+ 
    -5  -4  -3  -2  -1 
    """
)
print("Введите начальный и конечный индексы для того среза 'pizza', который хотите получить.")
print("Для выхода нажмите Enter, не вводя начальную позицию.")
start = None
while start != '':
    start = input('\nНачальная позиция: ')
    if start:
        start = int(start)
        finish = int(input("Конечная позиция: "))
        print("Срез word[", start, ":", finish, "] выглядит как", end=" ")
        print(word[start:finish])
