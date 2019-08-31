n=int(input());g=[list(input()) for _ in range(n)]
def bfs(i,j):
    q=__import__('collections').deque()
    q.append((i,j))
    c=0
    while q:
        x,y=q.popleft()
        if 0<=x-1 and g[x-1][y]=='1':
            q.append((x-1,y))
            g[x-1][y]='0'
        if x+1<n and g[x+1][y]=='1':
            q.append((x+1,y))
            g[x+1][y]='0'
        if 0<=y-1 and g[x][y-1]=='1':
            q.append((x,y-1))
            g[x][y-1]='0'
        if y+1<n and g[x][y+1]=='1':
            q.append((x,y+1))
            g[x][y+1]='0'
        c+=1
    if c==1: return 1
    else: return c-1
tot=0;r="";a=[]
for i in range(n):
    for j in range(n):
        if g[i][j]=='1':
            tot+=1;a.append(bfs(i,j))
r+=str(len(a))+'\n';a.sort()
r+='\n'.join(map(str,a))
print(r)
