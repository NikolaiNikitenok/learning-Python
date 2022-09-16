# Только согласные

# Демонстрирует, как создавать новые строки из исходных с помощью цикла for

message = input("Введите текст: ")
new_message = ""
VOMELS = "аеоиёоуыэяю"
print()
for letter in message:
    if letter.lower() not in VOMELS:
        new_message += letter
        print("Создана новая строка: ", new_message)
print("\nВот ваш текст с изъятыми гласными буквами: ", new_message)


