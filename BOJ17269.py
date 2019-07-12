d=[3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
n,m=map(int,input().split());a,b=input().split();s=""
while a!="" and b!="":
    s+=a[0]+b[0]
    a=a[1:];b=b[1:]
s+=a+b;t="";r=""
for i in s:
    t+=str(d[ord(i)-ord('A')])
for k in range(m+n-2):
    tmp=""
    for i in range(m+n-k-1):
        tmp+=str((int(t[i])+int(t[i+1]))%10)
    t=tmp
print(int(t),"%",sep="")
