input=__import__('sys').stdin.readline
n=int(input())
g=[[300000]*n for _ in range(n)]
for i in range(n):
    g[i][i]=0
for _ in range(int(input())):
    x,y,v=map(int,input().split())
    if g[x-1][y-1]!=300000:
        g[x-1][y-1]=min(g[x-1][y-1],v)
    else:
        g[x-1][y-1]=v
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j]=min(g[i][j],g[i][k]+g[k][j])
r=""
for i in range(n):
    for j in range(n):
        if g[i][j]==300000: r+='0 '
        else: r+=str(g[i][j])+' '
    r+='\n'
print(r.strip())
