a=[1,0,0];s=list(input())
for i in s:
    if i=='A':
        a[0],a[1]=a[1],a[0]
    elif i=='B':
        a[1],a[2]=a[2],a[1]
    else:
        a[2],a[0]=a[0],a[2]
for i in range(3):
    if a[i]==1: print(i+1)
