import math
n=int(input());r=""
for _ in range(n):
    a,b=map(int,input().split())
    c=math.gcd(a,b)
    r+=str((a//c)*b)+"\n"
print(r,end='')
