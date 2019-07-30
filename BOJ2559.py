n,k=map(int,input().split());a=[int(i) for i in input().split()];m=sum(a[:k]);s=m
for i in range(k,n):
    s+=(a[i]-a[i-k])
    if s>m:m=s
print(m)
