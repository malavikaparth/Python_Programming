# result = filter(function,list)
# to print filtyer we need to do result = list(filter(filter(function,list))

# LIST COMPREHENTION : [operation for element in list] OR
#                     [operation for element in list (if Condition)]
# eg:                  newList = [x+5 for x in aList]
# LAMBDA:            : (lambda arguments/s : operation)
# eg                   a = lambda x:x+5
#                     print(a(3)) : o/p : 8
# FILTER             : filter(function,list)
# eg: odd elements   : filter(lambdax:x%2!=0,aList)


# ENUMERATE EG:
def smallest(aList):
    small = aList[0]
    index = 0
    for i, j in enumerate(aList):
        if (i < small):
            small = i
            index = j
    return small, index


print(smallest([-1, 0, 1, 2, 3, 4]))

# 1.Write a list comprehension that replaces all elements in the list of numbers with their absolute value.
# [1,-1,3,-5] → [1,1,3,5]

alist = [1, -1, 3, -5]
print([abs(x) for x in alist])

# 2.Write a list comprehension that only contains the positive numbers occurring in a given list. [1,-1,3,-5]
# → [1,3]

aList = [1, -1, 3, -5]
aList2 = [x for x in aList if x > 0]
print(aList2)

# 3.Write a list comprehension that replaces all zeros in a list with -1. [1,0,3,0] → [1,-1,3,-1]

aList = [1, 0, 3, 0]
aList2 = [-1 if x == 0 else x for x in aList]
print(aList2)

# 4.#Write a list comprehension that converts all lowercase characters in a list to uppercase
# (other characters like space, coma,... should remain unchanged). [“a”, “b”, “C”] → [“A”, “B”, “C”]

aList = ["a", "b", "c"]
aList2 = [x.upper() if x.islower() else x for x in aList]
print(aList2)

# 5.Use a list comprehension to make a list of the first 10 powers of 2 starting from 1.
aList = [pow(2, x) for x in range(11)]
print(aList)

# 6. Use a list comprehension to remove empty lists from a list of lists. [ [], [0,1,2], [], [3,6,7,21] ] →
# [[0,1,2], [3,6,7,21]]

aList = [[], [0, 1, 2], [], [3, 6, 7, 21]]
aList2 = [x for x in aList if x != []]
print(aList2)

# 7.Use list comprehensions to convert a list of words to a list of tuples where each tuple contains the
# word and the length of the word. [‘Hello’, ‘Me’]→ [(‘Hello’,5),(‘Me’,2)

aList = ['Hello', 'Me']
aList2 = [len(x) for x in aList]
alist4 = [(x, len(x)) for x in aList]
print(alist4)

# 8. Use list comprehensions to replace all numbers ending with zero with zero in a list. [10, 1, 2, 100,
# 200] → [0, 1, 2, 0, 0]

aList = [10, 1, 2, 100, 200]
aList2 = [0 if x % 10 == 0 else x for x in aList]
print(aList2)

# 9. Use list comprehensions to use two lists (might be different length) and produce a list of all possible
# combinations of one element of each list. a = [“apple”, “pie”] b = [6, 7, 8, 9, 10] Output: [(‘apple’,6),
# (‘apple’,7), (‘apple’,8), (‘apple’,9), (‘apple’,10), (‘pie’,6), (‘pie’,7), (‘pie’,8), (‘pie’,9), (‘pie’,10)]

a = ["apple", "pie"]
b = [6, 7, 8, 9, 10]
c = []
for i in a:
    for j in b:
        c = c + [(i, j)]
print(c)
d = [(a_el, b_el) for a_el in a for b_el in b]
print(d)

# 10.Use list comprehensions to use two lists of the same length and produce a list of tuples
# with corresponding elements. For example: Two lists: a = [1, 2, 3, 4, 5] b = [6, 7, 8,
# 9, 10] Output: [(1, 6),(2, 7),(3, 8),(4, 9),(5, 10)]. BTW: python has builtin zip for this.

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = list(zip(a, b))
print(c)

# Filter and Lambda
# 1.Write a lambda function that increments its argument by one.
print((lambda x: x + 1)(3))

# 2. Write a lambda function that returns the sum of its two arguments.
print((lambda x, y: x + y)(2, 3))

# 3.Write a lambda function that returns the square root of its argument
import math

print((lambda x: math.sqrt(x))(36))

# 4.Write a lambda function that takes two arguments and returns the minimum.

print((lambda x, y: x if x < y else y)(9, 0))

# 5.Write a lambda function that returns the result of the expression x
# 2 + 2x−5 where x is its argument.

print((lambda x: x * x + 2 * x - 5)(10))

# 6.Use filter() to find intersection of the two lists: a=[1,2,3,5,7,9], b = [2,3,5,6,7,8].

a = [1, 2, 3, 5, 7, 9]
b = [2, 3, 5, 6, 7, 8]
result = list(filter(lambda x: x in a, b))
print(result)

# 7.. Write a program using lambda and filter which prints out all the even number between 1 and 20
# (both included).

# result = filter(function,list)

result = list(filter((lambda x: x % 2 == 0), [x for x in range(21)]))
print(result)

# 8.Write a program using lambda and filter which prints out only the positive numbers of the list: a =
# [-5,8,1,-3,10,-9]. Write the same using list comprehensions.

a = [5, 8, 1, -3, 10, -9]
result = list(filter((lambda x: x > 0), a))
print(result)

result2 = [x for x in a if x > 0]
print(result2)

# 9. REVERSING A LIST

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
backwards = lambda l: (backwards(l[1:]) + l[:1] if l else [])
print(backwards(mylist))
