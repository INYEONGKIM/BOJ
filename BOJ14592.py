class f:
    def __init__(self,i,s,c,d):
        self.i=i;self.s=s;self.c=c;self.d=d
l=[]
for i in range(int(input())):
    s,c,d=map(int,input().split())
    l.append(f(i,s,c,d))
l.sort(key=lambda x:(-x.s,x.c,x.d))
print(l[0].i+1)
