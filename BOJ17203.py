l,n=map(int,input().split())
a=[int(i) for i in input().split()];r=""
for _ in range(n):
    s=0
    x,y=map(int,input().split())
    for i in range(x,y):
        s+=abs(a[i]-a[i-1])
    r+=str(s)+"\n"
print(r,end="")
