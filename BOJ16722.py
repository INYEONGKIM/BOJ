class foo:
    def __init__(self,s,c,b):
        self.s=s
        self.c=c
        self.b=b
a=[]
for _ in range(9):
    s,c,b=input().split()
    a.append(foo(s,c,b))
ans=[]
for i in range(7):
    for j in range(i+1,8):
        for k in range(j+1,9):
            if (a[i].b==a[j].b==a[k].b or (a[i].b!=a[j].b and a[i].b!=a[k].b and a[j].b!=a[k].b)) \
                    and (a[i].s==a[j].s==a[k].s or (a[i].s!=a[j].s and a[i].s!=a[k].s and a[j].s!=a[k].s))\
                    and (a[i].c==a[j].c==a[k].c or (a[i].c!=a[j].c and a[i].c!=a[k].c and a[j].c!=a[k].c)):
                ans.append([i+1,j+1,k+1])
p=0;flag=False
for _ in range(int(input())):
    q=input().split()
    if q[0]=='G':
        if ans==[] and not flag:
            flag=True
            p+=3
        else:
            p-=1
    else:
        t=[int(q[1]),int(q[2]),int(q[3])]
        t.sort()
        if t in ans:
            ans.remove(t)
            p+=1
        else:
            p-=1
print(p)
