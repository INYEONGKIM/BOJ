input=__import__('sys').stdin.readline
n=int(input());g=[list(input().strip()) for _ in range(n)];t=[]
for i in range(n):
    t.append([])
    for j in range(n):
        s=g[i][j]
        if s=='G': t[i].append('R')
        else: t[i].append(s)

def bfs(i,j):
    q=[(i,j)];c=g[i][j];g[i][j]='X'
    while q!=[]:
        x,y=q[0];q=q[1:]
        for nx,ny in (x,y+1),(x,y-1),(x+1,y),(x-1,y):
            if nx>=0 and nx<n and ny>=0 and ny<n and g[nx][ny]==c:
                q.append((nx,ny))
                g[nx][ny]='X'
r1=0;r2=0
for i in range(n):
    for j in range(n):
        if g[i][j]!='X':
            bfs(i,j);r1+=1

def bfs2(i,j):
    q=[(i,j)];c=t[i][j];t[i][j]='X'
    while q!=[]:
        x,y=q[0];q=q[1:]
        for nx,ny in (x,y+1),(x,y-1),(x+1,y),(x-1,y):
            if nx>=0 and nx<n and ny>=0 and ny<n and t[nx][ny]==c:
                q.append((nx,ny))
                t[nx][ny]='X'
for i in range(n):
    for j in range(n):
        if t[i][j]!='X':
            bfs2(i,j);r2+=1
print(r1,r2)
