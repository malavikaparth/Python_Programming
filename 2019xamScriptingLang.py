# You are given a list of words and a string with a message. Write a function that verifies whether the given
# message can be reconstructed with the list of available words. Example:
# Given wordlist = [‘two’, ‘times’, ‘three’, ‘is’, ‘not’, ‘four’] and message = ‘two times two is four’, your
# function should return False.Explanation:
# The word ‘two’only occurs once in the wordlist, which means the message cannot be reconstructed.
def wordCheck(wordlist, message):
    s = ""
    message = message.split(" ")
    for i in message:
        if i in wordlist:
            wordlist.remove(i)
            s = True
        else:
            return False
    return s


wordlist1 = ['two', 'times', 'three', 'is', 'not', 'four']
message1 = 'two times two is four'
print(wordCheck(wordlist1, message1))


# You need to pay a certain amount of money. Assume you have an unlimited amount of banknotes of 20,
# 10 and 5 euros as well as coins of 2 euro, 1 euro, 50 eurocent, 20 eurocent and 10 eurocent. Write a
# function that returns the minimum amount of required banknotes and coins to pay the requested amount
# of money.
# Example 1:
# amount = 23.5, you function should return 4
# Explanation:
# The requested amount of money can be payed with one bill of 20, one coin of 2, one coin of 1 and one coin
# of 50 cent.
# Example 2:
# amount = 51, you function should return 4
# Explanation:
# The requested amount of money can be payed with two bills of 20, one bill of 10 and one coin of 1

def moneyCount(amount):
    l = [20, 10, 5, 2, 1, .50, .2, .1]
    count = 0
    res = 0
    i = 0
    while (amount > 0):
        if (amount >= l[i]):
            res = amount - l[i]
            count += 1
            amount = res
        else:
            # if(i<len(l)-1):
            i += 1
    return count


print(moneyCount(51))


# A modified Kaprekar number is a positive integer number with a special property. If you square it, then split
# the number into two integers and sum those integers, you have the same value you started with.
# Write a function that checks whether a number is a Kaprekar number and returns True or False accordingly.
# Note: one way to split an integer is to first convert it to a string and then converting those back to integers.
# Examples:
# For the number 45 your function should return True (45*45 = 2025 and 20+25 = 45)
# For the number 5 your function should return False (5*5 = 25 and 2+5=7 ≠ 5)
# For the number 11 your function should return False (11*11 = 121 and 12+1 ≠ 11 and 1+21≠

def modKaprekar(number):
    square = number ** 2
    square = str(square)
    length = len(square)
    sum1 = 0
    sum2 = 0
    mid = length // 2
    if (length % 2 != 0):
        sum1 += int(square[:mid]) + int(square[mid:])
        sum2 += int(square[mid:]) + int(square[:mid])
        if (sum1 != number and sum2 != number):
            return False
        else:
            return True
    else:
        sum1 += int(square[:mid]) + int(square[mid:])
        if (sum1 == number):
            return True
        else:
            return False


print(modKaprekar(15))
