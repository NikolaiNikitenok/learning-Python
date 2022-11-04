# Проверка работы библиотеки для перебора всевозможных комбинаций: itertools.  

import itertools

components = "1234567890qwertyuiopasdfghjklzxcvbnm"
combination = list(itertools.product(components, repeat=3))

print(combination)
