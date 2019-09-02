input=__import__('sys').stdin.readline
r,c=map(int,input().split());g=[list(input()) for _ in range(r)]
visited=[[False]*c for _ in range(r)]
def bfs(i,j):
    v=0;o=0;q=[]
    visited[i][j]=True
    q.append((i,j))
    while len(q):
        x,y=q.pop(0);t=g[x][y]
        visited[x][y]=True
        if t=='v': v+=1
        elif t=='o': o+=1
        for nx,ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
            if not (0<=nx<r and 0<=ny<c):
                continue
            if visited[nx][ny] or g[nx][ny]=='#':
                continue
            visited[nx][ny]=True
            q.append((nx,ny))
    if o>v: v=0
    elif v>0 and o<=v: o=0
    return v,o
totv=0;toto=0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and g[i][j]!='#':
            tv,to=bfs(i,j)
            totv+=tv;toto+=to
print(toto,totv)
