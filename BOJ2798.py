n,x=map(int, input().split())
res=0
l=[int(i) for i in input().split()]
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            s = l[i]+l[j]+l[k]
            if s<=x and x-s < x-res:
                res = s
print(res)
