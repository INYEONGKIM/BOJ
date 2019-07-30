import sys
n=int(sys.stdin.readline());a=[]
for _ in range(n):
    a.append([int(i) for i in sys.stdin.readline().split()])
for k in range(3):
    for i in range(n-1):
        t=a[i][k];f=False
        for j in range(i+1,n):
            if t==a[j][k]:
                a[j][k]=0;f=True
        if f: a[i][k]=0
r=""
for i in range(n):
    r+=str(sum(a[i]))+'\n'
print(r,end="")
