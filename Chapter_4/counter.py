# Считалка

# Демонстрирует использование функции range()

print('Посчитаем: ')
for i in range(10+1):
    print(i, end=' ')
print('\n\nПеречислим кратные пяти: ')
for i in range(0, 50+1, 5):
    print(i, end=' ')
print('\n\nПосчитаем в обратном порядке: ')
for i in range(10, 0, -1):
    print(i, end=' ')

for _ in range(10+1):
    print('Hallo!')
