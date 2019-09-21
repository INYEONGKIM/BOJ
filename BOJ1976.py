class f:
    def __init__(self,i,s):
        self.i=i;self.s=s
input=__import__('sys').stdin.readline
n=int(input());m=int(input())
sl=[f(i,{i}) for i in range(n)]

for i in range(n):
    t=input().split()
    for j in range(i):
        if t[j]=="1":
            aS,bS=set(),set();ai=bi=-1
            for x in range(len(sl)):
                if i in sl[x].s:
                    ai=x
                    aS=sl[x].s; continue
                elif j in sl[x].s:
                    bi=x
                    bS=sl[x].s; continue
            aS=set.union(aS,bS)
            if ai!=-1: sl[ai].s=aS
            if bi!=-1: sl.pop(bi)
f=True
t=[int(i)-1 for i in input().split()]
for s in sl:
    if f:
        if t[0] in s.s:
            for i in range(1,m):
                if not t[i] in s.s:
                    f=False
                    break
    else: break
print("YES" if f else "NO")
