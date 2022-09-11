import random

counter = 0
heads = 0
tails = 0
drop = 0

while counter != 100:
    drop = random.randint(1, 2)
    if drop == 1:
        heads += 1
        # print("Dropped head!")
    else:
        tails += 1
        # print("Dropped tail!")
    counter += 1
print("Coin tossed ", counter, " times!")
print("Heads dropped ", heads, " times!")
print("Tails dropped ", tails, " times!")
