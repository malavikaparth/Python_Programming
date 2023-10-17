# Define a	function shiftlist(alist, n) that	moves	the objects in a	list	alist to	the
# right	with	n positions.	For	example:	shiftlist([1,	2,	3,	4,	5],	1) should	return
# the	list	[5,	1, 2,	3,	4].
# Note:	take	into	account	that the	argument n can be	larger	than	the	length
# of	your	list:	i.e.	shiftlist([1,	2,	3,	4,	5],	1) and	shiftlist([1,	2,	3,	4,	5],	6) should
# produce	the	same	result

def shift(seq, n):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]


print(shift([1, 2, 3, 4], 5))

# Assume	you	are	given	a	text	file	that	has	the	following	content:
# . . . . . 1
# . 9 . . 4 .
# 2 . 8 . . .
# . . . 3 . .
# 0 1 . . . .
# . . . . . .
# And	you	are	given	the	function:
# def parsetxt(path):
# file = open(path, 'r')
# text = []
# for line in file:
# text.append(line)
# return text
# ANSWER :
['. . . . . 1\n', '. 9 . . 4 .\n', '2 . 8 . . .\n', '. . . 3 . .\n', '0 1 . . . .\n', '. . . . . .']


# b) Define a	function	that	prints	the	occurences of	digits	ranging	from	0	to	9
# in	the	file	above. Use	the	function	parsetxt for	reading	the	content	of
# the	file.	For	the	content given	above,	your	function	should	produce:

def parsetxt(path):
    file = open(path, 'r')
    data = file.read()
    data = data.split()
    for i in range(10):
        print(i, ":", data.count(str(i)))


parsetxt('matrix_1')

# i           0               1                 2                3               4
# j        0  1  2  3  4    0  1  2  3  4    0  1  2  3  4    0  1  2  3  4    0  1  2  3  4
myList = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 0, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 0]]
resLis = [[1, 2, 0, 4, 0], [1, 2, 0, 4, 0], [0, 0, 0, 0, 0], [1, 2, 0, 4, 0], [0, 0, 0, 0, 0]]

for row in myList:
    if any([value == 0 for value in row]):
        row[:] = [0] * len(row)

print(myList)
