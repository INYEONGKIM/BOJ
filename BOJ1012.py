input=__import__('sys').stdin.readline
__import__('sys').setrecursionlimit(10000)
r=""
def dfs(i,j):
    g[i][j]=False
    for nx,ny in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
        if nx>=n or nx<0 or ny<0 or ny>=m: continue
        if g[nx][ny]: dfs(nx,ny)

for _ in range(int(input())):
    m,n,k=map(int,input().split());g=[[False]*m for _ in range(n)]
    for _ in range(k):
        a,b=map(int,input().split())
        g[b][a]=True
    c=0
    for i in range(n):
        for j in range(m):
            if g[i][j]:
                dfs(i,j);c+=1
    r+=str(c)+'\n'
print(r,end="")
