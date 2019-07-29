n=int(input());a=[int(i) for i in input().split()];x=int(input());b=[int(i) for i in input().split()];r=""
d={}
for i in range(n):
    t=a[i]
    if t in d.keys():
        d[t]+=1
    else:
        d[t]=1
for i in range(x):
    t=b[i]
    if t in d.keys():
        r+=str(d[t])+" "
    else:
        r+="0 "
print(r,end="")
