x,y=map(int,input().split())
a=[];r=''
for _ in range(x):
    a.append(list(input()))
for k in range(y):
    for _ in range(x):
        for i in range(x-1):
            t=a[i][k];z=a[i+1][k]
            if t=='o' and z=='.':
                a[i][k]=z
                a[i+1][k]=t
for i in range(x):
    for j in range(y):
        r+=a[i][j]
    r+='\n'
print(r,end="")
