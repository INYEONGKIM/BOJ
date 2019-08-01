import sys
input=sys.stdin.readline
r=""
while True:
    n=int(input())
    if n==0: break
    a=[];b=[];t=n//2
    if n%2==1:
        t+=1
    for _ in range(t):
        a.append(input())
    for _ in range(n-t):
        b.append(input())
    for i in range(min(t,n-t)):
        r+=a[i]+b[i]
    if t!=n//2: r+=a[-1]
print(r,end="")
