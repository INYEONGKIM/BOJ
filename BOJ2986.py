import math
n=int(input()); r=int(math.sqrt(n)); k=1
for i in range(2,r+1):
    if n%i==0:
        k=max(i,n//i)
        break
print(n-k)
