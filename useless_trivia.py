# Бесполезные факты

# Узнает у пользователя его / ее личные данные и выдает несколько фактов
# о нем / ней. Эти факты истинны, но совершенно бесполезны.

name = input("Your Name? ")
age = int(input("How old? "))
weight = int(input("Your weight? "))
print("Your lower name: ", name.lower())
print("Your upper name: ", name.upper())

print("Called u: ", name * 5, sep=" ")
print("Your age in seconds: ", age * 365 * 23 * 60 * 60)

print("Your weight on Moon: ", weight / 6)
print("Your weight on Sun: ", weight * 27.1)

input("\n\nНажмите Enter, чтобы выйти.")
