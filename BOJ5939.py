import sys
input=sys.stdin.readline
a=[]
class f:
    def __init__(self,h,m,s,x):
        self.h=h
        self.m=m
        self.s=s
        self.x=x

for _ in range(int(input())):
    x=input();h,m,s=map(int,x.split());a.append(f(h,m,s,x))
a.sort(key=lambda z:(z.h,z.m,z.s));r=""
for i in a:
    r+=i.x
print(r.strip(),end="")
