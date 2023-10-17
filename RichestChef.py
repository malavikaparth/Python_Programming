#To take inout from user
t = int(input())
for value in range(1, t + 1):
    #Taking multiple input from user
    # N:denoting the maximum tastiness
    # s:the sum of tastiness of the two dishes
    # r:no more than RR days since his first dose
    diff = 0
    n, s = [int(x) for x in input().split()]
    for i in range(1,n+1):

        if((i-1) + i) == s:
            diff = i - (i-1)
            print(diff)
    print(abs(diff))
