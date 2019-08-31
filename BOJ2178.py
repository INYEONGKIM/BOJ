input=__import__('sys').stdin.readline
n,m=map(int,input().split());g=[list(input()) for _ in range(n)];c=[[0]*m for _ in range(n)]
q=__import__('collections').deque();q.append((0,0));c[0][0]=1
while q:
    x,y=q.popleft()
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0<=nx<n and 0<=ny<m and g[nx][ny]=='1' and c[nx][ny]==0:
            c[nx][ny]=c[x][y]+1
            q.append((nx,ny))
print(c[n-1][m-1])
