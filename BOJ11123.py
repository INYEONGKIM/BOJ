input = __import__('sys').stdin.readline

def dfs(i, j):
    stack = [(i, j)]; grid[i][j] = '.'
    while stack:
        i, j = stack.pop()
        for ni, nj in (i-1,j), (i,j-1), (i+1,j), (i,j+1):
            if 0<=ni<n and 0<=nj<m and grid[ni][nj] == '#':
                stack.append((ni,nj))
                grid[ni][nj] = '.'
    return 1

r=""
for TEST in range(int(input())):
    n, m = map(int,input().split())
    grid = [list(input().strip()) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#": ans+= dfs(i, j)
    r+=str(ans)+'\n'
print(r.strip())
