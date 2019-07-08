import math
n=int(input());r=""
for _ in range(n):
    r+=str(int((-1+math.sqrt(1+4*int(input())))/2))+'\n'
print(r,end="")
