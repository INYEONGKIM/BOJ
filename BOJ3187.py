input=__import__('sys').stdin.readline
r,c=map(int,input().split());g=[list(input()) for _ in range(r)];visited=[[False]*c for _ in range(r)]
totk=0;totv=0
def bfs(i,j):
    k=0;v=0
    visited[i][j]=True
    q=[];q.append((i,j))
    while len(q):
        x,y=q.pop(0)
        if g[x][y]=='v': v+=1
        elif g[x][y]=='k': k+=1
        for nx,ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
            if not(0<=nx<r and 0<=ny<c) or visited[nx][ny] or g[nx][ny]=='#': continue
            q.append((nx,ny))
            visited[nx][ny]=True
    if k>v: v=0
    else: k=0
    return k,v
for i in range(r):
    for j in range(c):
        if not visited[i][j] and g[i][j]!='#':
            tk,tv=bfs(i,j)
            totk+=tk; totv+=tv
print(totk,totv)
