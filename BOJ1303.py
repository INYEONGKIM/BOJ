input=__import__('sys').stdin.readline
n,m=map(int,input().split());g=[list(input()) for _ in range(m)];visited=[[False]*n for _ in range(m)]
b=0;w=0
def bfs(i,j):
    cnt=1
    col=g[i][j]
    visited[i][j]=True;q=[];q.append((i,j))
    while len(q):
        x,y=q.pop(0)
        if not visited[x][y]:
            visited[x][y]=True
            cnt+=1
        for nx,ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
            if not (0<=nx<m and 0<=ny<n): continue
            if visited[nx][ny] or g[nx][ny]!=col: continue
            q.append((nx,ny))
    if col=='W': return True,cnt*cnt
    else: return False,cnt*cnt
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            f,v=bfs(i,j)
            if f: w+=v
            else: b+=v
print(w,b)
