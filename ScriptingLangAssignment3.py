#Write the for loop below with a while loop:
#for k in range(9,0,-1):
#    print("k= ", k)

k = 9
while( k > 0):
    print("k= ", k)
    k-=1

#2)Write a function that returns the smallest and largest element in a list (without using the
#built-in Python functions and methods such as sort, min and max!). Note that the function
#returns two values!

def minMax(my_String):
    min = max = my_String[0]
    for i in my_String:
        if (i < min):
            min = i
        elif (i > max):
            max = i
    return min, max


print(minMax([1,9,8,7,6,5,3,4,0,2]))


#Nested lists

# Write a function that takes a nested list as argument, and returns the length of the longest
#list. For example: [[1,2,3],[4,5],[6,7,8,9],[10]]  4 since the longest list is [6,7,8,9] and its
#length is 4

def longList(myList):
    length = 0
    templen = 0
    for i in myList:
        templen = len(i)
        if (templen > length):
            length = templen
    return length



print(longList( [[1,2,3],[4,0,0,0,0,0,0,0,0,00],[5,6,7,8,9],[10]]))

#2. Write a function that has a nested list as an argument and calculates the averages of the jth
#elementsin each sub-list. Beware: the length of the list of averages should be as long as the
#longest sub-list! For example [[1,2,3], [4,5], [6,7,8,9], [10]] should return [5.25, 4.67, 5.5, 9.0]
#(calculated as follows[(1+4+6+10)/4, (2+5+7)/3, (3+8)/2 ,9/1]).

def averageLsit(myList):
    average = 0
    returnList = []
    length = longList(myList)
    for i in range(length): #VERY IMP!!!
        l = []
        for j in myList:
            if(i<len(j)): #VERY IMP!!!
               l.append(j[i])
            else:
                l.append(0)
        average = sum(l)/len(l)
        returnList.append(average)
    return returnList

my =  [[1,2,3], [4,5], [6,7,8,9], [10]]
print(averageLsit(my))

