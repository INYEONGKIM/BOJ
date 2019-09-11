l,c=map(int,input().split());a=list(input().split());a.sort();r=set()
def back(idx,cnt,s):
    if cnt==l:
        j=0;m=0
        for i in s:
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u": m+=1
            else: j+=1
        if j>=2 and m>=1: r.add(s)
        return
    for i in range(idx,c):
        back(i+1,cnt+1,s+a[i])
        back(i+1,cnt,s)
back(0,0,"");res=list(r);res.sort()
print('\n'.join(res))
