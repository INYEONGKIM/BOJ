r=""
while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    r+=str(a+b)+'\n'
print(r,end="")
