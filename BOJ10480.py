r=""
for _ in range(int(input())):
    x=int(input())
    if abs(x)%2==0:
        r+=str(x)+" is even\n"
    else:
        r+=str(x)+" is odd\n"
print(r,end="")
