n,x=map(int,input().split())
a=[int(i) for i in input().split()];a.sort()
while a!=[]:
    if x>=a[0]:
        x+=1;a=a[1:]
    else:
        break
print(x)
