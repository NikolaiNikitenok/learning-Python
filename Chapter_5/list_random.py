import random

list1 = ["list", "test", "block", "request"]
list2 = []
counter = len(list1)

while len(list2) != len(list1):
    slovo = random.choice(list1)
    if slovo not in list2:
        list2.append(slovo)
    else:
        continue

print(list2)
