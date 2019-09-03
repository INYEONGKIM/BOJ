input=__import__('sys').stdin.readline
n,m=map(int,input().split());d=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i==0 and j==0: continue
        elif i==0: d[i][j]+=d[i][j-1]
        elif j==0: d[i][j]+=d[i-1][j]
        elif i>0 and j>0: d[i][j]+=max(d[i-1][j-1],d[i][j-1],d[i-1][j])
print(d[n-1][m-1])
