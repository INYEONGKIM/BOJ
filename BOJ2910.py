class f:
    def __init__(self,n,c,i):
        self.n=n;self.c=c;self.i=i
n,c=map(int,__import__('sys').stdin.readline().split())
a=[int(i) for i in input().split()]
d={};r=""
for i in range(n):
    if a[i] in d:
        d[a[i]].c+=1
    else:
        d[a[i]]=f(a[i],1,i)
l=list(d.values());l.sort(key=lambda x:(-x.c, x.i))
for x in l:
    for i in range(x.c):
        r+=str(x.n)+' '
print(r.strip())
