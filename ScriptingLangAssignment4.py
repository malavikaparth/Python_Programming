# DICTIONARY EXAMPLE:
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')


# RECURSION
def sumList2(myList):
    sum = 0
    if (len(myList) == 1):
        sum = myList[0]
    else:
        sum = myList[0] + sumList2(myList[1:])
    return sum


print(sumList2([2, 3, 5, 6, 7, 8, 9, 12]))


# BUBBLE SORT
def bubbleSort(myList):
    for n in range(len(myList), 0, -1):
        for i in range(1, n):
            if myList[i] < myList[i - 1]:
                myList[i], myList[i - 1] = myList[i - 1], myList[i]
    return myList


mylist = [17, 34, 23, 35, 45, 9, 1]
print(bubbleSort(mylist))


# Write a recursive function that computes the factorial of a parameter n. Use the following
# formula:
# 𝑛! = 𝑛(𝑛 − 1)!

def fact(n):
    if (n == 1):
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))


# In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an efficient method for
# computing the greatest common divisor (GCD) of two numbers a and b, i.e. the largest
# number that divides both of them without leaving a remainder. Write a recursive function
# gcd that computes the greatest common divisor of two number by using Euclid’s algorithm.
# 𝑔𝑐𝑑(𝑎,𝑏) = {
#             𝑔𝑐𝑑(𝑏,𝑎 − 𝑏) 𝑖𝑓 𝑎 > 𝑏
#             𝑎 𝑖𝑓 𝑎 = 𝑏
#             𝑔𝑐𝑑(𝑎,𝑏 − 𝑎) 𝑖𝑓 𝑎 < b
#           }

def gcd(a, b):
    if (a == b):
        return a
    elif (a > b):
        return gcd(b, a - b)
    elif (a < b):
        return gcd(a, b - a)


print(gcd(8, 12))


# This function is supposed to return a string with a predefined number of ‘bla’.
def bla(amount):  # returns "bla" amount times
    i = 0
    resultString = ''
    while i < amount:
        resultString += 'bla'
        i += 1
    return resultString


print(bla(5))


# This function is supposed to check whether a list is sorted in increasing order. The result
# of this function should be a Boolean value.
def isSorted(mylist):
    for i in range(1, len(mylist)):
        first_element = mylist[i]
        second_element = mylist[i - 1]
    if (first_element <= second_element):
        return True
    else:
        return False


print(isSorted([4, 2, 1, 3]))


# which all elements in a list are divisible by 3

def f(myList, elements, divisor, start=0):
    count = 0
    b = elements
    if (start + elements <= len(myList)):
        for i in range(elements):
            if (myList[start + i] % divisor == 0 and myList[start + i] != 0):
                count += 1
    return count


print(f([4, 3, 2, 1], 2, 4, 0))

# You are given a text file ‘matrix1.txt’. This file contains the values of a 4x6 matrix. Write a
# function that storesthe values from this files into a two-dimensional(i.e. nested) list. This
# means you will end up with one variable that contains all the values. Make sure your function
# is able to read a matrix of any size

file = open('matrix_1', 'r')


def fileToList(fileName):
    l = []
    for line in fileName:
        l.append([line])
    return l


print(fileToList(file))


# Write a new function that writes a nested list to a file, organized in the same way as the data
# in ‘matrix1.txt’ (i.e. each row of the matrix will be a sub-list in your nested list). Test your
# function by writing the result of the function written in question 3a)to a new file.


def listToFile(myList):
    f = open('matrix_2', 'w')
    for i in myList:
        for j in i:
            f.write(j)


listToFile([['1 2 3 4 5 6\n'], ['7 8 9 10 11 12\n'], ['13 14 15 16 17 18\n'], ['19 20 21 22 23 24']])


# Same question when the /n is not i=given at the end

def listToFile2(myList):
    out = open('matrix_3', 'w')
    for i in myList:
        for j in range(len(i) + 1):
            if (j == len(i)):
                out.write('\n')
            else:
                out.write(i[j])


listToFile2([['1 2 3 4 5 6'], ['7 8 9 10 11 12'], ['13 14 15 16 17 18'], ['19 20 21 22 23 24']])
