n=int(input())
res=""
while n>0:
    n-=1
    a,b,c=map(int, input().split())
    if a==b-c:
        res+="does not matter\n"
    elif a>b-c:
        res+="do not advertise\n"
    else:
        res+="advertise\n"
print(res,end="")
