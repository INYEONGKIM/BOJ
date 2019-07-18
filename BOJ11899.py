s=input();sl=len(s);l=0;r=0
for i in range(sl):
    if s[i]==')':
        if r==0:
            l+=1
        else:
            r-=1
    else:
        r+=1
print(l+r)
