import random

list1 = []
list2 = []
userNumber1 = []
userNumber2 = []

def userlists (arg):
    global userNumber1
    global userNumber2
    
    if arg == list1:
        for i in range(0,10):
            userNumber1.append(int(input('Add a number to the first list: ')))
        arg = userNumber1
        return arg
    
    elif arg == list2:
        for i in range(0,10):
            userNumber2.append(int(input('Add a number to the second list: ')))
        arg = userNumber2
        return arg
        
    
    


def randomNumber ():
    numList = []

    for i in range(0,10):
        i = random.choice(range(0,1000))
        numList.append(i)

    return numList

list1 = userlists(list1)
list2 = userlists(list2)

