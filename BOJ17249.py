l,_,r=input().partition("(^0^)");lc=0;rc=0;ll=len(l);rl=len(r)
for i in range(ll):
    if l[i]=='@':
        if i+1<ll and l[i+1]=='=':
            lc+=1
for i in range(rl):
    if r[i]=='@':
        if i!=0 and r[i-1]=='=':
            rc+=1
print(lc,rc)
