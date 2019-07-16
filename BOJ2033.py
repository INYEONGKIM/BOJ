n=int(input());t=1
while n>10*t:
    n+=5*t;t*=10;n-=n%t
print(n)
