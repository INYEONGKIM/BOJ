import sys
input=sys.stdin.readline
t=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    if t%(b+a)<=b:
        t+=b-t%(b+a)+1
    else:
        t+=1
print(t)
