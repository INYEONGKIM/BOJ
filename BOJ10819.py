from itertools import permutations
n = int(__import__('sys').stdin.readline())
a = [int(_) for _ in __import__('sys').stdin.readline().split()]
res = -1
for x in permutations(a, n):
    r = 0
    for i in range(n-1):
        r += abs(x[i+1]-x[i])
    res = max(res, r)
print(res)
