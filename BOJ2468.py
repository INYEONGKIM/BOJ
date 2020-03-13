from collections import deque

n=int(__import__('sys').stdin.readline())
a = [[int(i) for i in input().split()] for _ in range(n)]

max_height = -1
for x in a:
    max_height = max(max(x), max_height)

max_island = -1
for height in range(max_height):
    visited = [[False if a[i][j] > height else True for j in range(n)] for i in range(n)]
    res = 0
    q = deque()
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                res += 1
                q.append((i,j))
                while q:
                    x, y = q.pop()
                    visited[x][y] = True
                    for (_x, _y) in (x-1, y), (x, y+1), (x+1, y), (x, y-1):
                        if not (0 <= _x < n and 0 <= _y < n):
                            continue
                        else:
                            if not visited[_x][_y]:
                                q.append((_x, _y))
    max_island = max(res, max_island)
print(max_island)
