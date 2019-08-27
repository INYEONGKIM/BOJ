input=__import__('sys').stdin.readline
x,y=map(int,input().split());a=[int(i) for i in input().split()];b=[int(i) for i in input().split()]
res="";i=0;j=0
while i<x and j<y:
    if a[i]<b[j]:
        res+=str(a[i])+' ';i+=1
    else:
        res+=str(b[j])+' ';j+=1
if i==x:
    while j<y:
        res+=str(b[j])+' ';j+=1
else:
    while i<x:
        res+=str(a[i])+' ';i+=1
print(res.strip())
