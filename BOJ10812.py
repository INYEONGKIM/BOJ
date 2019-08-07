k,n=map(int,input().split());a=[int(i+1) for i in range(k)]
for _ in range(n):
    s,e,m=map(int,input().split())
    b0=a[:s-1];b1=a[s-1:e];b2=a[e:];a=[]
    l=b1[:m-s];r=b1[m-s:];b1=r+l
    a=b0+b1+b2
r=""
for i in a:
    r+=str(i)+' '
print(r)
