import random

MINIMUM = 1
MAXIMUM = 45

number = int(input("How many quick picks?"))
for i in  range(1,number+1):
    list = []
    for i in  range(1,7):
        random_Number = random.randrange(MINIMUM, MAXIMUM)
        while random_Number in list:
            random_Number = random.randrange(MINIMUM, MAXIMUM)
        list.append(random_Number)
    list.sort()
    print(" ".join("{}".format(random_Number) for random_Number in list))