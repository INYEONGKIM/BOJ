import math
a,b=map(int, input().split()); c=math.gcd(a,b)
print(a//c * b//c * c)
