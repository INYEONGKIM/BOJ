a=[1,1,2,4];n=int(input());t=3;r=""
for _ in range(n):
    x=int(input())
    if x>t:
        for i in range(t+1,x+1):
            a.append(a[i-1]+a[i-2]+a[i-3]+a[i-4])
        t=x
    r+=str(a[x])+"\n"
print(r,end="")
