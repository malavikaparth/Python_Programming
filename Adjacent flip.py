t = int(input())
for value in range(1, t + 1):
    n = int(input())
    s = str(input())
    count = 0
    S = [int(i) for i in str(s.zfill(n - 1))]
    s1 = []
    if (len(S) == 1):
        for i in range(len(S)):
            if (S[i] == 1):
                count = 1
                break
            else:
                count = 0
    else:
        for i in range(n):
            if (S[i] == 1):
                s1.append(i)
            else:
                count = 0
        for i in range(len(s1) - 1):
            if (s1[i + 1] != (s1[i] + 1)):
                 count = 1
            else:
                 count = 2
                 break
    print(count)
