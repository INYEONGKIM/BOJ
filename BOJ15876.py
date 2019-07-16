n,x=map(int,input().split());r="";cnt=0;idx=0;turn=1
if n==1 and x==1:
    r="0 1 1 0 1"
else:
    if n==x:
        x=0
    while cnt!=5:
        t=bin(idx);t=t[2:];l=len(t)
        for i in range(l):
            if turn==x:
                cnt+=1
                r+=t[i]+" "
                if cnt==5: break
            turn=(turn+1)%n
        idx+=1
print(r)
