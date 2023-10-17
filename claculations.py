# Python3 code to demonstrate
# conversion of number to list of integers
# using map()

# initializing number
num = str(0000)

# printing number
print("The original number is " + num.zfill(3))

# using map()
# to convert number to list of integers
res = list(map(int, str(num.zfill(3))))

# printing result
print("The list from number is " + str(res))