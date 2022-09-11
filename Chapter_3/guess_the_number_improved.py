import random

attempts = 7
number = random.randint(1, 100)
guess = int(input('Your guess? '))
print('Your attempts: ', attempts)

while attempts > 0 and guess != number:
    if guess > number:
        print('Less...')
    else:
        print('More...')
    guess = int(input('Your guess? '))
    attempts -= 1
    print('Your attempts: ', attempts)

if attempts < 0:
    print('Game Over!!!')
else:
    print('You are WINNER!!!!')
50