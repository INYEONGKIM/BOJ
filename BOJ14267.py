__import__('sys').setrecursionlimit(10**7)
from collections import deque
n, cnt = map(int, __import__('sys').stdin.readline().split())
root = -1
hit = [0] * (n + 1)
dic = [deque([]) for _ in range(n+1)]
for idx, x in enumerate(map(int, __import__('sys').stdin.readline().split())):
    if x != -1:
        dic[x].append(idx+1)
    else:
        root = idx+1

for _ in range(cnt):
    tar, dam = map(int, __import__('sys').stdin.readline().split())
    hit[tar] += dam

def dfs(v):
    for u in dic[v]:
        hit[u] += hit[v]
        dfs(u)

dfs(root)

print(' '.join(map(str, hit[1:])))
