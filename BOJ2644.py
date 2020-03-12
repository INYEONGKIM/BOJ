from collections import deque
n=int(__import__('sys').stdin.readline())
me, target = map(int, __import__('sys').stdin.readline().split())
me -= 1; target -= 1
graph = [[False]*n for _ in range(n)]
for _ in range(int(__import__('sys').stdin.readline())):
    p, c = map(int,__import__('sys').stdin.readline().split())
    graph[p-1][c-1] = True
    graph[c-1][p-1] = True
visited = [False]*n
visited[me] = True
q = deque()
q.append((me, 0))
res = -1
while q:
    who, depth = q.popleft()
    visited[who] = True
    if who == target:
        res = depth
        break
    for idx in range(n):
        if graph[who][idx] and not visited[idx]:
            q.append((idx, depth+1))
print(res)
