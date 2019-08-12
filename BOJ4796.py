import sys
r="";i=1
while True:
    l,p,v=map(int,sys.stdin.readline().split())
    if l==0==p==v: break
    t=(v//p)*l
    if v%p>l: t+=l
    else: t+=v%p
    r+="Case "+str(i)+": "+str(t)+'\n'
    i+=1
print(r,end="")
