#  Доступ отовсюду

# Демонстрирует работу с глобальными переменными


def read_global():
    print("В области видимости функции read_global() значение value равно", value)


def shadow_global():
    value = -10
    print("В области видимости функции shadow_global() значение value равно", value)


def change_global():
    global value
    value = -10
    print("В области видимости функции change_global() значение value равно", value)


# Основная часть

# value - глобальная переменная, потому что сейчас находится в глобальной области видимости

value = 10
print(
    "В глобальной области видимости значение переменной value сейчас стало равным",
    value,
    "\n",
)
read_global()
print(
    "Вернемся в глобальную область видимости. Здесь value по-прежнему равно",
    value,
    "\n",
)
shadow_global()
print(
    "Вернемся в глобальную область видимости. Здесь value по-прежнему равно",
    value,
    "\n",
)
change_global()
print("Вернемся в глобальную область видимости. Значени value стало равно", value, "\n")
input("\n\nPress Enter!")
