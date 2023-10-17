# List comprehension is an elegant way to define and create a list in python.
# We can create lists just like mathematical statements and in one line only.
# Negative value of steps shows right to left traversal instead of left to right traversal that is why [: : -1]
# prints list in reverse order.

## TYPES:
# [x*x for x in alist]
# [x*x for x in alsit if x>0]
# [x*x if x>0 else x*2 for x in alsit]


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# LIST COMPREHENTION
list3 = [i + j for i in list1 for j in list2]
print(list3)

# Given a two Python list. Write a program to iterate both lists simultaneously and display
# items from list1 in original order and items from list2 in reverse order.

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i, j in zip(list1, list2[::-1]):
    print(i, j)

# List of all even squares less than 1000
list1 = [x ** 2 for x in range(1, 1001) if x % 2 == 0]
print(list1)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Print all elements
fruits1 = [x for x in fruits]
print(fruits1)

# Only accept items that are not "apple":
fruits1 = [x for x in fruits if x != "apple"]
print(fruits1)

# Accept only numbers lower than 5:
list1 = [x for x in range(0, 5)]
print(list1)

list2 = [x for x in range(10) if x < 5]
print(list2)

# Set the values in the new list to upper case:

alist = ['apple', 'orange', 'grapes']
list1 = [x.upper() for x in alist]
print(list1)

# Set all values in the new list to 'hello':

alist = ['apple', 'orange', 'grapes']
print(alist)
list1 = ['hello' for x in alist]
print(list1)

# Return "banana" instead of "orange":

alist = ['apple', 'orange', 'grapes']
list1 = ['banana' if x == 'orange' else x for x in alist]
print(list1)

# Iterating through a string Using List Comprehension
string = 'human'
letters = [x for x in string]
print(letters)

# below list contains square of all odd numbers from
# range 1 to 10

list10 = [x ** 2 for x in range(1, 11) if x % 2 != 0]
print(list10)

# below list contains power of 2 from 1 to 8
list2 = [2 ** i for i in range(1, 9)]
print(list2)

# list for lowering the characters
listLow = [x.lower() for x in ["A", "B", "C"]]
print(listLow)

# list which extracts number
string = "my phone number is : 11122 !!"
listEx = [x for x in string if x.isdigit()]
print(listEx)

# A list of list for multiplication table
a = 4
listMul = [x * a for x in range(1, 11)]
print(listMul)

list10 = [x for x in range(1, 11)]
#  below list has numbers from 2 to 5
print(list10[1:5])
#  below list has numbers from 6 to 8
print(list10[5:8])
#  below list has numbers from 2 to 10
print(list10[1:10])
#  below list has numbers from 1 to 5
print(list10[:5])
#  below list has numbers from 2 to 8 in step 2
print(list10[1:5:2])
#  below list has numbers from 10 to 1
print(list10[::-1])
#  below list has numbers from 10 to 6 in step 2
print(list10[9:3:-2])

# List of square of even numbers less thatn 1000
list1 = [x * x for x in range(1000) if x * x % 2 == 0 and x * x < 1000]
print(list1)


import functools
#  filtering odd numbers
oddList = filter(lambda x: x % 2 != 0, range(1, 11))
print(list(oddList))

#  filtering odd square which are divisible by 5
oddListSq = filter(lambda x: x % 5 == 0, [x ** 2 for x in range(1, 11) if x % 2 != 0])
print(list(oddListSq))

#   filtering negative numbers
negalist = filter(lambda x:x<0,range(-5,5))
print(list(negalist))

#  implementing max() function,
reduceMax = functools.reduce(lambda x,y:x if x>y else y , [7, 12, 45, 100, 15])
print(reduceMax)

a = ["apple" , "pie"]
b = [5,6,7,8,9]
list1 = [(i,j) for i in a for j in b]
print(list(list1))

x = 1
y = 1
z = 1
n = 2
new_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k != n)]
print(new_list)