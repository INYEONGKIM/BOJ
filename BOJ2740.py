n,m=map(int,input().split());a=[];r=[];res=""
for i in range(n):
    a.append([int(j) for j in input().split()])
m,k=map(int,input().split());b=[]
for i in range(m):
    b.append([int(j) for j in input().split()])
for i in range(n):
    r.append([0]*k)
for i in range(n):
    for j in range(k):
        for x in range(m):
            r[i][j]+=a[i][x]*b[x][j]
        res+=str(r[i][j])
        if j<k-1:
            res+=" "
        else:
            res+="\n"
print(res,end="")
