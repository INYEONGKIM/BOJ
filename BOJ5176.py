import sys
input=sys.stdin.readline
r=""
for _ in range(int(input())):
    p,k=map(int,input().split());a=[1 for _ in range(k)];c=0
    for _ in range(p):
        t=int(input())-1
        if a[t]==1: a[t]-=1
        else: c+=1
    r+=str(c)+'\n'
print(r,end="")
