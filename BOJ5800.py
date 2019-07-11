n=int(input());r=""
for k in range(1,n+1):
    a=[int(i) for i in input().split()];g=-1;al=a[0];a=a[1:];a.sort()
    for i in range(0,al-1):
        if a[i+1]-a[i]>g:
            g=a[i+1]-a[i]
    r+="Class "+str(k)+"\nMax "+str(a[-1])+", Min "+str(a[0])+", Largest gap "+str(g)+"\n"
print(r,end="")
