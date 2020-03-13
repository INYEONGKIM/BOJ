from collections import deque
m, n = map(int, __import__('sys').stdin.readline().split())
a = [[int(_) for _ in __import__('sys').stdin.readline().split()] for _ in range(n)]
visited = [[False if a[i][j] == 0 else True for j in range(m)] for i in range(n)]

day = -1
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            q.append((i, j))
while q:
    l = len(q)
    for _ in range(l):
        i, j = q.popleft()
        for x, y in (i-1, j), (i, j+1), (i+1, j), (i, j-1):
            if not(0 <= x < n and 0 <= y < m):
                continue
            else:
                if not visited[x][y]:
                    visited[x][y] = True
                    q.append((x, y))
    day += 1

chk = True
for x in visited:
    if False in x:
        chk = False
        break

if chk: print(day)
else: print(-1)
