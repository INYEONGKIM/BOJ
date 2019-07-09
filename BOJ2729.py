n=int(input());r=""
for _ in range(n):
    s=input().split()
    a=int(s[0],2)
    b=int(s[1],2)
    r+=bin(a+b)[2:]+'\n'
print(r,end="")
