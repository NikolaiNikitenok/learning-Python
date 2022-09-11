import random

print('Guess the number.')
input('Are you ready? Pls, press "Enter"!')

minimum = 1
maximum = 100
guess = random.randint(minimum, maximum)
print(guess)
answer = input('How? ')

while answer != '=':
    if answer == '<':
        minimum = guess + 1
        guess = random.randint(minimum, maximum)
        print(guess)
    elif answer == '>':
        maximum = guess - 1
        guess = random.randint(minimum, maximum)
        print(guess)
    answer = input('How? ')
print('Your number = ', guess)
