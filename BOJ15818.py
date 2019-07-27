n,x=map(int,input().split());a=[int(i) for i in input().split()];t=a[0]%x
for i in range(1,n):
    t=(a[i]*t)%x
print(t)
