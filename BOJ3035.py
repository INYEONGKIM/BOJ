r,c,zr,zc=map(int,input().split());a=[];res=""
for i in range(r):
    a.append(input())
for i in range(r*zr):
    for j in range(c*zc):
        res+=a[i//zr][j//zc]
    res+='\n'
print(res,end="")
