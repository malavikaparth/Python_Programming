# The filter() method filters the given sequence with the help of a function that
# tests each element in the sequence to be true or not.

print(list(filter(lambda x: x > 2, [1, 3, 1, 3, 4, 1, ])))  # O/P : [3, 3, 4]

print(set(filter(lambda x: x > 2, [1, 3, 1, 3, 4, 1, ])))  # O/P : {3, 4}


# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)
print(list(filtered))

# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

oddseq = filter(lambda x: x % 2 != 0, seq)
print(list(oddseq))

# result contains even numbers of the list
evenseq = filter(lambda x: x % 2 == 0, seq)
print(list(evenseq))
