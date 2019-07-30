n,m=map(int,input().split());a=set(int(i) for i in input().split());b=set(int(i) for i in input().split());a-=b
r=str(len(a));a=list(a);a.sort()
if a!=[]:
    r+='\n'
    for i in a:
        r+=str(i)+' '
print(r)
