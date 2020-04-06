__import__('sys').setrecursionlimit(10**6)
n, m = map(int, __import__('sys').stdin.readline().split())
visited = [[True if x is '0' else False for x in __import__('sys').stdin.readline().split()] for _ in range(n)]
cnt = 0

def dfs(x, y):
    visited[x][y] = True
    for _x, _y in (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y - 1):
        if (0 <= _x < n and 0 <= _y < m) and not visited[_x][_y]:
            dfs(_x, _y)
        else:
            continue

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1
print(cnt)
