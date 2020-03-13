__import__('sys').setrecursionlimit(10**9)

n=int(__import__('sys').stdin.readline())
a = [[int(i) for i in input().split()] for _ in range(n)]

max_height = -1
for x in a:
    max_height = max(max(x), max_height)


def dfs(i, j):
    visited[i][j] = True
    for (x, y) in (i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1):
        if not (0 <= x < n and 0 <= y < n):
            continue
        else:
            if not visited[x][y]:
                dfs(x, y)

max_island = -1
for height in range(max_height):
    visited = [[False if a[i][j] > height else True for j in range(n)] for i in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                res += 1
                dfs(i, j)
    max_island = max(res, max_island)
print(max_island)
