class foo:
    def __init__(self,s,i):
        self.s=s
        self.i=i
import sys
input=sys.stdin.readline;r=""
while True:
    n=int(input())
    if n==0:
        break
    a=[];t=[]
    for i in range(n):
        s=input()
        a.append(foo(s.lower(),i))
        t.append(s)
    a.sort(key=lambda x:x.s)
    r+=t[a[0].i]
print(r,end="")
