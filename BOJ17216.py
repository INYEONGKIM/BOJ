n=int(input());a=list(map(int,input().split()));d=[0]*n;r=1
for i in range(n):
    d[i]=a[i]
    for j in range(n):
        if a[i]<a[j] and d[i]<=d[j]+a[i]:
            d[i]=d[j]+a[i]
    r=max(r,d[i])
print(r)
