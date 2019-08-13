n=int(input());r=0;i=1
while i*i<n:
    if n%i==0:
        r+=i
        r+=n//i
    i+=1
if i*i==n: r+=i
print(r*5-24)
