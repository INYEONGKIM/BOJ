n=int(input());a=[int(i) for i in input().split()];cnt=0;a.append(0);a.append(0)
for i in range(n):
    if a[i]==1:
        cnt+=1
        if a[i+1]==1: a[i+1]=0
        else: a[i+1]=1
        if a[i+2]==1: a[i+2]=0
        else: a[i+2]=1
print(cnt)
