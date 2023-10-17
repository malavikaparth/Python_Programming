import functools
print(functools.reduce(lambda a, b: a + b,[(lambda x: x ** x)(x) for x in list(filter(lambda x: (x % 2 == 0), [x for x in range(0, 5)]))]))