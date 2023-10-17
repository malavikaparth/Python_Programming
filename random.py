mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = list()
rotated = list(zip(*mylist))[::-1]
print(rotated)
