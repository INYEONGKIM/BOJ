n=int(input());a=[int(i) for i in input().split()]
d=[1 for _ in range(n)]
for i in range(1, n):
    for j in range(0, i):
        if a[i]>a[j] and d[i]<=d[j]:
            d[i]=d[j]+1
        elif a[i]==a[j]:
            d[i]=d[j]
print(max(d))
