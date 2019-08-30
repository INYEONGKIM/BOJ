input=__import__('sys').stdin.readline
n=int(input());m=int(input());g=[[0]*n for _ in range(n)]
for _ in range(m):
    x,y=map(int,input().split())
    g[x-1][y-1]=1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k]==1 and g[k][j]==1: g[i][j]=1
r=""
for i in range(n):
    c=0
    for j in range(n):
        if g[i][j]==0 and g[j][i]==0: c+=1
    r+=str(c-1)+'\n'
print(r,end="")
