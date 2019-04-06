x,y = map(int, input().split())
a = []
b = []
for i in range(x):
    a.append([int(j) for j in input().split()])
for i in range(x):
    b.append([int(j) for j in input().split()])

res=""
for i in range(x):
    for j in range(y):
        res+=str(a[i][j] + b[i][j])
        if j!=y-1:
            res+=" "
    res+="\n"
print(res,end="")
