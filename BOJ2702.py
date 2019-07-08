import math
n=int(input());r=""
for _ in range(n):
    a,b=map(int,input().split())
    g=math.gcd(a,b)
    r+=str(a//g*b)+" "+str(g)+'\n'
print(r,end="")
