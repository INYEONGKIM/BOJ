r,c,m = -1,-1,-1
l=[]
for i in range(9):
    l.append([int(i) for i in input().split()])
    if m < max(l[i]):
        m=max(l[i]); r=i; c=l[i].index(m)
print(m)
print(r+1,c+1)
