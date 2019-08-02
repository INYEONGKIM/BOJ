n,m=map(int,input().split())
a=[False]*(n+1);s=0
b=[int(i) for i in input().split()]
for i in b:
    t=i
    while t<=n:
        a[t]=True
        t+=i
for i in range(2,n+1):
    if a[i]:
        s+=i
print(s)
