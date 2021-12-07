def Convert(n):
    n = iter(n)
    n = dict(zip(n, n))
    return n
n = ['a', 1, 'b', 2, 'c', 3]
print(Convert(n))