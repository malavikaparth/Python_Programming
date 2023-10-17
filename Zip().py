# Python zip() method takes iterable or containers and returns a single iterator object,
# having mapped values from all the containers.
# It is used to map the similar index of multiple containers so that they can
# be used just using a single entity.

# Example 1: Python zip two lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]

zipped = zip(name, roll_no)
print(list(zipped))

# Python zip enumerate

names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (names, ages) in enumerate(zip(names, ages)):
    print(i, names, ages)

# Python zip() Dictionary

stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

# Create a dictionary
# [operation for element in list]
stocks_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(stocks_dict)

# How to unzip?
# Unzipping means converting the zipped values back to the individual self as they were.
# This is done with the help of “*” operator.

# Python code to demonstrate the working of
# unzip

# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
zip_val = zip(name, roll_no, marks)
zip_val = list(zip_val)
print(zip_val)

# UNZIPPING
names, roll_nos, marks = zip(*zip_val)

print("The name list is : ", end="")
print(names)

print("The name list is : ", end="")
print(roll_nos)

print("The name list is : ", end="")
print(marks)

# Practical Applications
# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.

for p, s in zip(players, scores):
    print("player", p, "scores", s)
