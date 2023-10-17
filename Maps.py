# Map is a function that applies a function to each element of the list and
# stores the results in a new list.

def myMaps(f, alist):
    return [f(x) for x in alist]


print(myMaps(lambda x: x * 2, [1, 2, 3, 4]))
print(myMaps(lambda x: x > 2, [1, 2, 3, 4]))

# TO NOTE
y = [1, 2, 3, 4]
z = map(lambda x: x * 2, y)
print(z)
print(list(z))

#
addi = map(lambda x: x + x, [1, 2, 3, 4])
print(list(addi))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

resList = map(lambda x, y: x + y, numbers1, numbers2)
print(list(resList))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
z = map(list,l)
print(list(z))
