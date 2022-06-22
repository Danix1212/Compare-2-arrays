import random


def randomNumber ():
    numList = []

    for i in range(0,10):
        i = random.choice(range(0,1000))
        numList.append(i)

    return numList

list1 = randomNumber()
list2 = randomNumber()

