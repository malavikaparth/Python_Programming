# Python Lambda Functions

# Python Lambda Functions are anonymous function means that the function is without a name.
# As we already know that the def keyword is used to define a normal function in Python.
# Similarly, the lambda keyword is used to define an anonymous function in Python.

# SYNTAX : lambda arguments: expression

# This function can have any number of arguments but only one expression, which is evaluated and returned.
# One is free to use lambda functions wherever function objects are required.
# You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
# It has various uses in particular fields of programming besides other types of expressions in functions.

# 1.
a = lambda str: str

print(a("hello"))


# 2
def test(f, a, b):
    return f(a, b)


print(test(lambda x, y: x + y, 1, 2))
print(test(lambda x, y: x * y, 1, 2))

# 3
# These are actually function
square = lambda x: x ** 2
cube = lambda x: x ** 3

print("square of 2", square(2))
print("cube of 2", cube(2))


# 4.
# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube1(y):
    return y * y * y


cube2 = lambda x: x ** 3

print(cube1(3))
print(cube2(2))

# Example 1: Python Lambda Function with List Comprehension

# We will try to print the table of 10.

table10 = [lambda x=x: x * 10 for x in range(1, 11)]

for t in table10:
    print(t())

# Example 2: Python Lambda Function with if-else
f = lambda a, b: a if (a > b) else b

print(f(1, 2))

# Example 3: Python Lambda with Multiple statements
# Lambda functions does not allow multiple statements, however,
# we can create two lambda functions and then call the other lambda function as a parameter
# to the first function.

# Let’s try to find the second maximum element using lambda.

List1 = [[2, 4, 3], [16, 64, 1, 4], [3, 12, 9, 6]]

# sorting list
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]

resList = secondLargest(List1, sortList)
print(list(resList))

# Using lambda() Function with filter()

# Here is a small program that returns the odd numbers from an input list:

# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
offli = filter(lambda x: x % 2 != 0, li)
print(list(offli))

# Python code to print people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]
allow = filter(lambda x: x > 18, ages)
print(list(allow))

# Using lambda() Function with map()

# Python code to illustrate
# map() with lambda()
# to get double of a list.

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
doubleli = map(lambda x: x * 2, li)
print(list(doubleli))

# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']

# here we intend to change all animal names
# to upper case and return the same

animals2 = map(lambda x: x.upper(), animals)
print(list(animals2))

# Using lambda() Function with reduce()
# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2, ]
# using reduce to compute sum of list
sumList = functools.reduce(lambda x: x + x, lis)
print(list(sumList))
