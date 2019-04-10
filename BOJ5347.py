import math
res=""
n=int(input())
while n>0:
    n-=1
    a,b=map(int, input().split())
    c=math.gcd(a,b)
    res+=str((a//c)*b)+"\n"
print(res,end="")
