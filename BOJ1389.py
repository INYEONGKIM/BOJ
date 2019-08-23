input=__import__('sys').stdin.readline
n,e=map(int,input().split());g=[[0]*n for _ in range(n)]
for _ in range(e):
    a,b=map(int,input().split())
    g[a-1][b-1]=1;g[b-1][a-1]=1
z=[n-1]*n
for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k]!=0 and g[k][j]!=0:
                if g[i][j]==0: g[i][j]=g[i][k]+g[k][j]
                else: g[i][j]=min(g[i][j],g[i][k]+g[k][j])
m=__import__('sys').maxsize;idx=-1
for i in range(n):
    t=sum(g[i])
    if m>t: m=t;idx=i+1
print(idx)
