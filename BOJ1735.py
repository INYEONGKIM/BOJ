import math
a,b=map(int,input().split());c,d=map(int,input().split());y=b//math.gcd(b,d)*d;x=a*(y//b)+c*(y//d);t=math.gcd(x,y)
if t!=1:
    x//=t;y//=t
print(x,y)
