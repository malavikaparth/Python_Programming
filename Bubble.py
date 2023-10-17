import math

def bubbleSort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if(a[i]>a[i+1]):
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    return a




