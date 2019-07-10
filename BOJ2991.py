a,b,c,d=map(int,input().split())
d1=a+b;d2=c+d;r=""
x=[int(i) for i in input().split()]
for i in range(3):
    cnt=0
    if (x[i]-1)%d1<a:
        cnt+=1
    if (x[i]-1)%d2<c:
        cnt+=1
    r+=str(cnt)+'\n'
print(r)
