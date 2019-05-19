n=int(input())
r=""
while n>1:
    r+=str(n)+" "
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
r+=str(n)
print(r)
