n=int(input());top=0
for _ in range(n):
    a=[0]*6;s=[int(i) for i in input().split()]
    for i in range(4):
        a[s[i]-1]+=1
    t=max(a);tmp=0
    if t==4:
        tmp=50000+s[0]*5000
    elif t==3:
        tmp=10000+(a.index(3)+1)*1000
    elif t==2:
        ts=set(s)
        if len(ts)==2:
            tmp=2000+500*(sum(s)//2)
        else:
            tmp=1000+100*(a.index(2)+1)
    else:
        tmp=100*max(s)
    if tmp>top: top=tmp
print(top)
