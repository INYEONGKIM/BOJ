m,n=map(int,input().split());d=[]
for i in range(m):
    if i==0:
        d.append([1]*n)
    else:
        t=[1];t+=[0]*(n-1)
        d.append(t)
for i in range(1,m):
    for j in range(1,n):
        d[i][j]=(d[i-1][j-1]+d[i-1][j]+d[i][j-1])%(1e9+7)
print(int(d[-1][-1]))
