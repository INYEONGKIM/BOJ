import math
n=int(input())
res=""
l = [int(i) for i in input().split()]
a=l[0]
for i in range(1,n):
    b=math.gcd(a,l[i])
    res+=str(a//b)+"/"+str(l[i]//b)+"\n"
print(res,end="")
