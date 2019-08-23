input=__import__('sys').stdin.readline
n=int(input());x=[list(map(int,input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if x[i][k]==1 and x[k][j]: x[i][j]=1
r=""
for i in range(n):
    r+=' '.join(map(str,x[i]))+'\n'
print(r,end="")
