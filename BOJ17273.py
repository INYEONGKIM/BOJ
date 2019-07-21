class card:
    def __init__(self,f,b,pos,flag):
        self.f=f
        self.b=b
        self.pos=pos
        self.flag=flag
d=[]
n,m=map(int,input().split())
for i in range(n):
    f,b=map(int,input().split())
    d.append(card(f,b,f,True))
for i in range(m):
    x=int(input())
    for c in d:
        if c.pos<=x:
            if c.flag:
                c.pos=c.b
                c.flag=False
            else:
                c.pos=c.f
                c.flag=True
r=0
for i in d:
    r+=i.pos
print(r)
