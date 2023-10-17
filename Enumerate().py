# Often, when dealing with iterators, we also get a need to keep a count of iterations.
# Python eases the programmers’ task by providing a built-in function enumerate() for this task.
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
# This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.

# SYNTAX
# enumerate(iterable, start=0)

# Parameters:
# Iterable: any object that supports iteration
# Start: the index value from which the counter is
#              to be started, by default it is 0


# python
# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print(list(obj1))
print(list(obj2))

## changing start index to 2 from 0
obj2 = enumerate((s1), start=2)
print(list(obj2))


#Using Enumerate object in loops:
# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for n in enumerate(l1):
    print(n)

# changing index and printing separately

for i, j in enumerate(l1, start=100):
    print("index:", i, "value", j)

#getting desired output from tuple
for i, j in enumerate(l1, start=100):
    print("index" , i)
    print("value",j)