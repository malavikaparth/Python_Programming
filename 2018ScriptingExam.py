# You are given two lists. Write a function that returns the difference between these two lists. Your function
# should return a list.Note: the order in which the elements appear in the resulting list do not matter.
# Example:For the lists [0, 1, 2, ‘a’] and [‘b’, 0, 2] your function should return [‘a’, 1, ‘b’].
# Explanation: ‘a’ and 1 do not appear in the second list, ‘b’ does not appear in the first list.

def differenceList(aList1, aList2):
    diff1 = list(set(aList1) - set(aList2))
    diff2 = list(set(aList2) - set(aList1))
    diff1.extend(diff2)
    return diff1


aList1 = [0, 1, 2, 'a']
aList2 = ['b', 0, 2]
print(differenceList(aList1, aList2))


# The Collatz Conjecture or 3x+1 problem can be summarized as follows:
# Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to
# get 3n + 1. Repeat the process indefinitely. The conjecture states that no matter which number you start
# with, you will always reach 1 eventually.
# Write a function that implements the following: given a number n, return the number of steps required  to reach 1.
# Example: For n = 5 your function should return 5.
# Step 1: 5  3x5+1 = 16
# Step 2: 16 16/2 = 8
# Step 3: 8  8/2 = 4
# Step 4: 4  4/2 = 2
# Step 5: 2  2/2 = 1

def collecCon(n):
    count = 0
    while (n >= 1):
        if (n % 2 == 0):
            n = n / 2
            count += 1
        elif (n == 1):
            return count
        else:
            n = 3 * n + 1
            count += 1


print(collecCon(6))


# RECURSION
# Write a function find_max that returns the largest element in a list by using recursion.
def find_max(seq):
    if len(seq) == 1:
        return seq[0]
    else:
        if seq[0] > seq[1]:
            seq.pop(1)
        else:
            seq.pop(0)
        return find_max(seq)


print(find_max([2, 3, 11, 6, 7, 10]))
