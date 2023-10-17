def parsetxt(path):
    file = open(path, 'r')
    data = file.read()
    data = data.split()
    print(data)
    for i in range(10):
        print(i,":",data.count(str(i)))

parsetxt('matrix_1')
