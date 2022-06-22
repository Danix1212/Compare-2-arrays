from randomizer import list1, list2

biggestNumber1 = 0
biggestNumber2 = 0

def getBiggestNumber (arg):
    global biggestNumber1 , biggestNumber2

    for number in arg: # Get the biggest number for each array
        if arg == list1:
            if number > biggestNumber1:
                biggestNumber1 = number
            else:
                pass
        elif arg == list2:
            if number > biggestNumber2:
                 biggestNumber2 = number
            else:
                pass

def kingNumber (arg1, arg2):
    number = 0

    if arg1 > arg2: # Compare
        number = arg1
    else:
        number = arg2

    return number

getBiggestNumber(list1)
getBiggestNumber(list2)

biggestNumber = kingNumber (biggestNumber1, biggestNumber2)

print(f'The first array is: {list1}')
print(f'The second array is: {list2}\n')

print(f'The biggest number from the first array is: {biggestNumber1}\n')
print(f'The biggest number from the second array is: {biggestNumber2}\n')

print(f'The biggest number between the two is: {biggestNumber}')

# No Googling was used in the making of this programme :P