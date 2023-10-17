# Write a function that swaps the element at every even index n with the (n+1)th element in a
# list. For example: given the list [0, 1, 2, 3, 4, 5] your function should return [1, 0, 3, 2, 5, 4].

def switchList(mylist):
    for i in range(0, len(mylist), 2):
        mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
    return mylist


myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(switchList(myList))


# Write a function that splits a list every nth element. For example: Given the list ['a', 'b', 'c', 'd',
# 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'] and n=3, your function should return
# [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

def splitList(aList, n):
    res = []
    for i in range(1, n + 1):
        res.append([])
    for j in range(n):
        res[j] = aList[j::n]
    return res


mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(splitList(mylist, 3))
