n=int(input());r=int(input());r-=n;x=1
n+=r-1
if n//2<r:
    r=n-r
for i in range(r):
    x*=n-i;x/=(1+i)
print(int(x))
