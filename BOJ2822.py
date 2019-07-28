class f:
    def __init__(self,v,i):
        self.v=v
        self.i=i
a=[];s=0;id=[]
for i in range(1,9):
    a.append(f(int(input()),i))
a.sort(key=lambda x:x.v)
for i in range(3,8):
    s+=a[i].v
    id.append(a[i].i)
id.sort()
print(s)
for x in id:
    print(x,end=" ")
