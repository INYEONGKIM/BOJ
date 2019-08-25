class f:
    def __init__(self,t,q,p):
        self.t=t;self.q=q;self.p=p
input=__import__('sys').stdin.readline
n,x=map(int,input().split());d={};a=[]
for _ in range(n):
    u,t,q,p=input().split()
    if u not in d.keys():
        d[u]=f(t,int(q),int(p))
    else:
        if d[u].q<int(q) or (d[u].q==int(q) and d[u].p>int(p)):
            d[u]=f(t,int(q),int(p))
for i in d.values():
    a.append(i)
a.sort(key=lambda v:(-v.q, v.p));r=""
for i in range(x):
    r+=a[i].t+'\n'
print(r,end='')
