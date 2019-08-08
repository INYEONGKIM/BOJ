import sys
input=sys.stdin.readline
n,c=map(int,input().split());x=[0]*n
for _ in range(c):
    a,b=map(int,input().split())
    x[a-1]+=1;x[b-1]+=1
r=""
for i in x:
    r+=str(i)+'\n'
print(r,end="")
