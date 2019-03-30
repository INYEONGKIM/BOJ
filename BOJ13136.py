r,c,n = map(int, input().split())
res=0
if r%n==0:
    res += r//n
else:
    res += r//n+1
if c%n==0:
    res *= c//n
else:
    res *= c//n+1
print(res)
