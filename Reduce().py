# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2, ]
# using reduce to compute sum of list
sumList = functools.reduce(lambda x: x + x, lis)
print(list(sumList))

# python code to demonstrate working of reduce()


# initializing list
lis = [1, 3, 5, 6, 2, ]
# using reduce to compute sum of list
sumList = functools.reduce(lambda x, y: x + y, lis)
print((sumList))

# using reduce to compute maximum element from list
maxList = functools.reduce(lambda x, y: x if x > y else y, lis)
print(maxList)

import functools


def all(sequence):
    return functools.reduce(lambda x, y: x and y, sequence, True)


print(all([False, True, False]))


def allPositive(sequence):
    return all(map(lambda x: x > 0, sequence))


print(allPositive([False, True, False]))

import functools

aList = [1, -2, 3, -4]
z = functools.reduce(lambda x, y: x > 0 and y, aList,True)
print(z)
#WORKING : 1 and reduce(-2,3,-4) =>T
#              -2 and reduce(3,-4) =>F
#                3 and reduce(-4) =>T
#                 -4 and reduce([]) =>F
#

