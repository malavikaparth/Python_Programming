def create_corners(n, numx):
    corners = numx * ('#' + '-' * n) + '#\n'
    return corners


def create_central(n, numx):
    central = numx * ('|' + ' ' * n) + '|\n'
    return central


def create_grid(n, m, numx):
    grid = numx * (create_corners(n, numx) + m * create_central(n, numx)) + create_corners(n, numx)
    return grid


# print(create_corners(3))
# print(create_central(3))
print(create_grid(3, 3, 3))


######################################################
def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


print(leapYear(2041))


def leapYear(year):
    if (year % 4 == 0):
        if (year % 100 != 0):
            return True
    elif (year % 400 == 0):
        return True;
    else:
        return False;


print(leapYear(1997))


def printBlaFor(n):
    for i in range(1, n + 1):
        print("bla")


printBlaFor(3)


def printPattern(n):
    for i in range(1, n, 1):
        print("*" * i)
    for j in range(n, 0, -1):
        print("*" * j)


printPattern(4)


def printBlaWhile(n):
    while (n > 0):
        print("bla")
        n -= 1


printBlaWhile(4)


def printPatterWhile(n):
    i = 1;
    while (i < n):
        print("*" * i)
        i += 1
    while (i > 0):
        print("*" * i)
        i -= 1


print(printPatterWhile(4))


def devision(div, dev):
    q = div / dev
    r = div % dev
    return (q, r)


print(devision(4, 2))


def listOfPowers(n, num):
    powerList = []
    prod = 1
    # powerList.append(prod)
    for i in range(1, n + 1, 1):
        prod *= num
        powerList.append(prod)
    return powerList


print(listOfPowers(3, -4))


def averageFinder(myList):
    sumav = 0
    for i in myList:
        sumav += i
    average = sumav / len(myList)
    return average


def reverseLsit(myList):
    reverseList = []
    for i in range(1, len(myList) + 1):
        reverseList.append(myList[len(myList) - i])
    return reverseList


myList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(reverseLsit(myList))


def palindromCheck(str):
    for i in range(len(str) // 2):
        if (str[i] == str[-1 - i]):
            return True
        else:
            return False


s = "motor"
print(palindromCheck(s))
