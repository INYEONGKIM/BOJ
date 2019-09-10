n=int(input());d=[[0]*3 for _ in range(n)]
d[0][0]=0
d[0][1]=1
d[0][2]=1
for i in range(1,n):
    for j in range(3):
        d[i][j]=int((d[i-1][0]+d[i-1][1]+d[i-1][2])%(1e9+9))
print(d[n-1][0])
