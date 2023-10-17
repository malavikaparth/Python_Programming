t = int(input())
for value in range(1,t+1):
   x, y = [int(x) for x in input().split()]
   if(x>y):
       print(x-y)
   else:
       print(y-x)
