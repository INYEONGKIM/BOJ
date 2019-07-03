c,s=input().split();r="";l=len(s)
if c=='D':
    for i in range(l//2):
        r+=s[2*i]*int(s[2*i+1])
else:
    t=s[0];cnt=1
    for i in range(1,l):
        if t==s[i]:
            cnt+=1
        else:
            r+=t+str(cnt)
            cnt=1
        t=s[i]
    r+=t+str(cnt)
print(r)
