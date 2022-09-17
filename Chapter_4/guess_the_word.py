import random

WORDS = ("вечеринка", "компьютер", "телефон", "портфель", "слово", "секрет")

correct = random.choice(WORDS)

count = 5
while count != 0:
    letter = input("Your letter: ")
    if letter in correct:
        print("Yes")
    else:
        print("No")
    count -= 1

guess = input("Your word: ")

while guess != correct:
    print("Incorrect!!! Try again")
    guess = input("Your word: ")
    if guess == '':
        print("U lose! Correct word was: ", correct)
        break

if guess == correct:
    print("U WINNER!!!! Correct word was: ", correct)
