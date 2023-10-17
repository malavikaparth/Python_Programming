t = int(input())
for value in range(1, t + 1):
    alist = []
    n = int(input())
    for i in range(0, n):
        a = int(input())
        alist.append(a)
    for i in alist:
        check = alist[i]
        for j in range(i+1,n):
            if(alist[j] >= 1 and alist[j] < alist[j+1] and alist[j+1] < n):
                print(j,j+1)
