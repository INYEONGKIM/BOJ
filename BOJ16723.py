n=int(input());r=0;k=2
n*=2
while n>=k:
    r+=k*(n//k-n//(2*k))
    k*=2
print(r)
