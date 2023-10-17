# SELECTION SORT

def selectionSort(my_List):
    for n in range(0, len(my_List), 1):
        smallest = my_List[n]
        index = n #To keep track of the position of smallest element in list so that it gets swaped correctly
        for i in range(n, len(my_List), 1):
            if (my_List[i] < smallest):
                smallest = my_List[i]
                index = i
        my_List[index] = my_List[n]
        my_List[n] = smallest
    return my_List


myList = [34, 17, 23, 35, 45, 9, 1]
print(selectionSort(myList))
